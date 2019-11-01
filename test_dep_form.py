#!/usr/bin/env python

import unittest
import dep_form_use_case


class DepFormTest(unittest.TestCase):
    def test_dep_calc_ul(self):
        self.assertEqual(dep_form_use_case.dep_calc_ul(), True)



if __name__ == "__main__":
    unittest.main()