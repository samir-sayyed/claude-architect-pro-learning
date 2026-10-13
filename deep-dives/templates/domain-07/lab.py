#!/usr/bin/env python3
"""Offline retry lab: Python 3.9+, no credentials, network, or file writes.

buggy intentionally fails its business invariant; fixed must pass all checks.
shortcut: in-memory, single-process ledger; use durable atomic storage for production.
"""

import argparse
import hashlib


class Provider:
    def __init__(self):
        self.charges = {}
        self.lose_first_reply = True

    def charge(self, key, amount_cents):
        if key in self.charges:
            if self.charges[key] != amount_cents:
                raise ValueError("existing key has a different amount")
            return {"status": "succeeded", "key": key}
        self.charges[key] = amount_cents
        if self.lose_first_reply:
            self.lose_first_reply = False
            raise TimeoutError("provider committed; response was lost")
        return {"status": "succeeded", "key": key}


class Checkout:
    def __init__(self, provider, mode):
        self.provider = provider
        self.mode = mode
        self.intents = {}
        self.attempt_number = 0

    def pay(self, tenant, order, amount_cents):
        if not tenant or not order or type(amount_cents) is not int or amount_cents <= 0:
            raise ValueError("tenant, order and positive integer cents required")
        identity = (tenant, "charge", order)
        previous = self.intents.get(identity)
        if previous is not None and previous != amount_cents:
            raise ValueError("same business intent cannot change its amount")
        self.intents[identity] = amount_cents
        stable_key = hashlib.sha256(repr(identity).encode("utf-8")).hexdigest()
        for _ in range(2):
            self.attempt_number += 1
            key = stable_key
            if self.mode == "buggy":
                key = f"{stable_key}-attempt-{self.attempt_number}"
            try:
                return self.provider.charge(key, amount_cents)
            except TimeoutError:
                pass
        raise TimeoutError("bounded retries exhausted; reconcile before another action")


def check(mode):
    provider = Provider()
    checkout = Checkout(provider, mode)
    checkout.pay("tenant-a", "order-42", 1200)
    checkout.pay("tenant-a", "order-42", 1200)
    assert len(provider.charges) == 1, (
        f"one business intent created {len(provider.charges)} charges; expected 1"
    )
    assert sum(provider.charges.values()) == 1200, "one order must charge 1200 cents"
    checkout.pay("tenant-b", "order-42", 1200)
    assert len(provider.charges) == 2, "distinct tenants must not collapse into one payment"
    before = dict(provider.charges)
    try:
        checkout.pay("tenant-a", "order-42", 1300)
    except ValueError:
        pass
    else:
        raise AssertionError("changed payload must be rejected")
    assert provider.charges == before, "rejected payload must cause no side effect"
    for bad_amount in (0, -1, 12.5, True):
        try:
            checkout.pay("tenant-a", "invalid", bad_amount)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid money input accepted")
    print("PASS: one intent/one charge, tenant scope, payload conflict, money validation")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("buggy", "fixed"))
    check(parser.parse_args().mode)
