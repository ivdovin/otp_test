#!/usr/bin/env python

import unittest
import test_dep_form


test_load = unittest.TestLoader()
suite = test_load.loadTestsFromModule(test_dep_form)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
