#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import unittest

from hypothesis import given

from hypothesis_strategies import list_of_ints_or_lists_of_ints
from list_unroller import unroll_nested_lists


class TestListUnroller(unittest.TestCase):

    @given(list_of_ints_or_lists_of_ints())
    def test_unroller_generated(self, lst):
        result = unroll_nested_lists(lst)

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, (int, long))

        # validation against stringified form.
        comparison = [
            long(i.strip()) if 'L' in i else int(i)
            for i in re.sub(r'\[|\]', '', str(result)).split(',') if i
        ]

        self.assertEqual(result, comparison)

    def test_unroller_regression(self):
        """ some specific examples to stand beside the generated tests """
        self.assertEqual(unroll_nested_lists([]), [])
        self.assertEqual(unroll_nested_lists([0]), [0])
        self.assertEqual(unroll_nested_lists([[3]]), [3])
        self.assertEqual(unroll_nested_lists([1, 2, [3]]), [1, 2, 3])
        self.assertEqual(unroll_nested_lists([[1, 2, [3]], 4]), [1, 2, 3, 4])
