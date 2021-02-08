from cube import *

import unittest

class CubeTestCase(unittest.TestCase):
    
    def testCubeVolume(self):
        self.assertEqual(40, cubeVolume(4,2,5))
        self.assertRaises(ValueError, cubeVolume, 7+2j,1+0j,1+4j)
        self.assertRaises(ValueError, cubeVolume, 4, -3, -2)

if __name__ == "__main__":
    unittest.main()
