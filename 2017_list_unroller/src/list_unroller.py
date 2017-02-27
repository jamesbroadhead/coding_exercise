#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Write some code, that will flatten an array of arbitrarily nested arrays of integers into a flat array of integers. e.g. [[1,2,[3]],4] -> [1,2,3,4].
"""


def unroll_nested_lists(list_of_items):
    """
    @param list_of_items: list of either integers, or nested lists of integers of
    arbitrary depth

    @return list<int>, containing the integers from the nested list, in the order
    they appeared in the nested list
    """
    output = []
    for item in list_of_items:
        if not isinstance(item, (int, long)):
            output.extend(unroll_nested_lists(item))
        else:
            output.append(item)
    return output
