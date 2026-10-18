#!/usr/bin/env python3
"""Rebuild the portable sections and check repository navigation."""
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
        self.ids = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and 'href' in attrs:
            self.hrefs.append(attrs['href'])
        if tag in ('img', 'script') and 'src' in attrs:
            self.hrefs.append(attrs['src'])
        if 'id' in attrs:
            self.ids.append(attrs['id'])


def verify():
    parsed = {}
    for path in ROOT.rglob('*.html'):
        page = Links()
        page.feed(path.read_text())
        assert len(page.ids) == len(set(page.ids)), ('Duplicate IDs', path)
        parsed[path.resolve()] = page
    for path, page in parsed.items():
        for href in page.hrefs:
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            assert target.is_relative_to(ROOT), ('Outside repository', path, href)
            assert target.is_file(), ('Missing local target', path, href)
            if url.fragment and target in parsed:
                assert unquote(url.fragment) in parsed[target].ids, ('Missing fragment', path, href)
    assert len(list((ROOT / 'learning').glob('ep*.html'))) == 11
    assert not list(ROOT.glob('ep*.html')), 'Episode pages belong only in learning/'
    assert len(parsed) == 75
    assert not list(ROOT.rglob('*.pdf')), 'The official PDF must not be distributed'
    assert not (ROOT / 'raw').exists() and not (ROOT / 'wiki').exists()
    print('PASS: 74 rendered HTML pages plus exam template, four study sections, local assets, eleven exam sets and public artifact boundaries; no root episode files.')


if __name__ == '__main__':
    for section in ('learning', 'mock-exams/ccar-p', 'deep-dives', 'mock-exams/core-concept-learning'):
        subprocess.run([sys.executable, str(ROOT / section / 'build.py')], check=True)
    verify()
