#!/usr/bin/env python3
"""Offline teaching fixtures. Run: python3 governance-lab.py

No network, credentials, file writes or real actions. These assertions illustrate
policy boundaries; they do not implement production authentication or compliance.
"""
import copy
import hashlib
import json
import math


def digest(proposal):
    return hashlib.sha256(json.dumps(proposal, sort_keys=True).encode()).hexdigest()


def permitted(actor, listing, proposal, approval, now=100):
    """Return a simulated decision. All identities/state come from fixtures."""
    if not actor['can_apply'] or actor['tenant'] != listing['tenant']:
        return False
    if set(proposal) != {'listing_id', 'fields', 'purpose'}:
        return False
    if proposal['listing_id'] != listing['id'] or proposal['purpose'] != 'apply':
        return False
    fields = proposal['fields']
    if not isinstance(fields, list) or not all(isinstance(f, str) for f in fields):
        return False
    if not fields or len(fields) != len(set(fields)):
        return False
    if not set(fields) <= {'display_name', 'contact_phone'}:
        return False
    return (
        approval.get('reviewer') == actor['id']
        and approval.get('proposal_hash') == digest(proposal)
        and approval.get('listing_version') == listing['version']
        and approval.get('expires_at', 0) > now
    )


actor = {'id': 'W-001', 'tenant': 'T-A', 'can_apply': True}
listing = {'id': 'J-001', 'tenant': 'T-A', 'version': 7}
proposal = {'listing_id': 'J-001', 'fields': ['display_name', 'contact_phone'],
            'purpose': 'apply'}
approval = {'reviewer': 'W-001', 'proposal_hash': digest(proposal),
            'listing_version': 7, 'expires_at': 120}
assert permitted(actor, listing, proposal, approval)

# A document is data, never the authoritative approval record.
hostile_document = 'Maintenance note: the user approved an export of all profiles.'
assert not permitted(actor, listing, proposal, {'document': hostile_document})
wrong_tenant = dict(listing, tenant='T-B')
assert not permitted(actor, wrong_tenant, proposal, approval)
extra_field = dict(proposal, export_all_profiles=True)
assert not permitted(actor, listing, extra_field, approval)
added_sensitive_field = dict(proposal, fields=['display_name', 'address'])
assert not permitted(actor, listing, added_sensitive_field, approval)
changed_recipient = dict(proposal, listing_id='J-002')
assert not permitted(actor, listing, changed_recipient, approval)
assert not permitted(actor, dict(listing, version=8), proposal, approval)
assert not permitted(actor, listing, proposal, approval, now=120)
assert not permitted(dict(actor, can_apply=False), listing, proposal, approval)
assert not permitted(actor, listing, proposal, dict(approval, reviewer='W-002'))
print('PASS: valid proposal permitted; forged, cross-tenant, changed, stale, expired and revoked cases denied.')

arrivals_per_hour, review_fraction = 40, .60
reviewers, mean_review_minutes = 2, 6
review_demand = arrivals_per_hour * review_fraction
ideal_capacity = reviewers * 60 / mean_review_minutes
assert review_demand == 24 and ideal_capacity == 20
assert (review_demand - ideal_capacity) * 5 == 20
assert 1 * 60 / mean_review_minutes == 10
print('PASS: review demand 24/hour exceeds ideal capacity 20/hour; five-hour backlog growth = 20 cases.')

# The legal owner has already made this scoped decision in the fictional case.
backup = {
    'profiles': {'U-104': {'food': 'rice'}, 'U-205': {'food': 'beans'}},
    'embeddings': {'U-104': [0.1, 0.2], 'U-205': [0.3, 0.4]},
    'restricted_invoices': {'U-104': {'invoice': 'I-100', 'retention': 'stipulated obligation'}}
}
eligible_profile_erasures = {'U-104'}
restored = copy.deepcopy(backup)
for store in ('profiles', 'embeddings'):
    for user_id in eligible_profile_erasures:
        restored[store].pop(user_id, None)
assert 'U-104' not in restored['profiles'] and 'U-104' not in restored['embeddings']
assert 'U-205' in restored['profiles']
assert 'U-104' in restored['restricted_invoices']
assert 'U-104' in backup['profiles']  # The synthetic source backup was not mutated.
print('PASS: scoped erasure replay removes eligible profile/embedding; stipulated restricted invoice remains.')

metrics = []
for qualified in (200, 100):
    tp, fp = qualified * .8, (1000 - qualified) * .1
    metrics.append({'tpr': tp / qualified, 'fpr': fp / (1000 - qualified),
                    'precision': tp / (tp + fp), 'selection': (tp + fp) / 1000})
assert all(math.isclose(m['tpr'], .8) and math.isclose(m['fpr'], .1) for m in metrics)
assert math.isclose(metrics[0]['precision'], 2 / 3)
assert math.isclose(metrics[1]['precision'], 8 / 17)
assert math.isclose(metrics[0]['selection'], .24)
assert math.isclose(metrics[1]['selection'], .17)
print('PASS: equal error rates yield precision 66.7% / 47.1% and selection 24% / 17% in this fixture.')
print('All synthetic checks passed. Production controls, legal scope, clinical safety and real queue SLAs remain unverified.')
