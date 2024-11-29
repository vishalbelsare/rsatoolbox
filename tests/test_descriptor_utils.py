#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_descriptor_utils
Test for descriptor utils
@author: adkipnis
"""

import unittest
import numpy as np


class TestDescriptorUtils(unittest.TestCase):

    def test_format_descriptor(self):
        from rsatoolbox.util.descriptor_utils import format_descriptor
        descriptors = {'foo': 'bar', 'foz': 12.3}
        self.assertEqual(
            format_descriptor(descriptors),
            'foo = bar\nfoz = 12.3\n'
        )

    def test_parse_input_descriptor(self):
        from rsatoolbox.util.descriptor_utils import parse_input_descriptor
        descriptors = {'foo': 'bar', 'foz': 12.3}
        self.assertEqual(
            parse_input_descriptor(descriptors),
            descriptors
        )
        self.assertEqual(
            parse_input_descriptor(None),
            {}
        )

    def test_append_descriptor(self):
        from rsatoolbox.util.descriptor_utils import append_descriptor
        desc = {'index': np.arange(3),
                'test1': [1, 3, 2],
                'test2': ['a', 'b', 'c']}
        desc_app = append_descriptor(desc, desc)
        assert np.all(desc_app['test1'] == np.array([1, 3, 2, 1, 3, 2]))
        assert np.all(desc_app['test2']
                      == np.array(['a', 'b', 'c', 'a', 'b', 'c']))

    def test_check_descriptor_length(self):
        from rsatoolbox.util.descriptor_utils import check_descriptor_length
        descriptors = {'foo': ['bar', 'bar2']}
        assert check_descriptor_length(descriptors, 2)
        assert not check_descriptor_length(descriptors, 3)
        descriptors = {'foo': ['bar']}
        assert check_descriptor_length(descriptors, 1)

    def test_check_descriptor_length_0d(self):
        """numpy casts str to 0d arrays (arrays with empty shape).
        This breaks things."""
        from rsatoolbox.util.descriptor_utils import check_descriptor_length
        descriptors = {'foo': 'bar'}
        assert check_descriptor_length(descriptors, 1)

    def test_subset_descriptor(self):
        from rsatoolbox.util.descriptor_utils import subset_descriptor
        descriptors = {'foo': ['bar', 'bar2']}
        self.assertEqual(
                subset_descriptor(descriptors, 0),
                {'foo': ['bar']}
                )
        self.assertEqual(
                subset_descriptor(descriptors, (0, 1)),
                {'foo': ['bar', 'bar2']}
                )

    def test_check_descriptor_length_error(self):
        from rsatoolbox.util.descriptor_utils import check_descriptor_length_error
        descriptors = {'foo': ['bar', 'bar2']}
        check_descriptor_length_error(descriptors, 'test', 2)

    def test_desc_eq(self):
        from rsatoolbox.util.descriptor_utils import desc_eq
        from numpy import array
        self.assertTrue(desc_eq(
            dict(abc=['a', 'b', 'c'], idx=array([1.1, 2.2])),
            dict(abc=['a', 'b', 'c'], idx=array([1.1, 2.2])),
        ))
        self.assertFalse(desc_eq(
            dict(abc=['a', 'b', 'c'], idx=array([1.1, 2.2])),
            dict(abc=['a', 'b', 'c'], idx=array([1.1, 3.3])),
        ), 'desc_eq should be False if an array element is different')
        self.assertFalse(desc_eq(
            dict(abc=['a', 'b', 'c'], idx=array([1.1, 2.2])),
            dict(abc=['a', 'b', 'D'], idx=array([1.1, 3.3])),
        ), 'desc_eq should be False if a list element is different')
        self.assertFalse(desc_eq(
            dict(abc=['a', 'b', 'c'], idx=array([1.1, 2.2])),
            dict(abc=['a', 'b', 'c'], idx=array([1.1, 2.2]), foo=[4, 5]),
        ), 'desc_eq should be False if the keys are different')
