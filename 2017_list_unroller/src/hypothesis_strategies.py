#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom strategies for hypothesis generated tests
"""
from hypothesis import strategies


def list_of_ints_or_lists_of_ints():
    return strategies.recursive(strategies.lists(elements=strategies.integers()), strategies.lists)
