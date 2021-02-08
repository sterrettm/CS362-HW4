from name import *

import unittest

class NameTestCase(unittest.TestCase):

    def testCombineNames(self):
        self.assertEqual("John Smith", combineNames("John","Smith"))
        self.assertRaises(ValueError, combineNames, "Samuel", "")
        self.assertRaises(TypeError, combineNames, "Andrew", [4,1,8])


if __name__ == "__main__":
    unittest.main()
