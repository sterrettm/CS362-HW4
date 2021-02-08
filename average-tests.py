from average import *

import unittest

class AverageTestCase(unittest.TestCase):

    def testAverage(self):
        self.assertEqual(6, average([4,2,12]))
        self.assertEqual(3+2j, average([4+1j, 3+2j, 2+3j]))
        self.assertEqual(0, average([]))
    

if __name__ == "__main__":
    unittest.main()
