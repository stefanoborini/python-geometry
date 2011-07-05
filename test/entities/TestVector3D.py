# @author Stefano Borini
import os; import sys; script_path=sys.path[0]; sys.path.append(os.path.join(script_path, "../../../"));
import unittest

from geometry import entities
import math

class TestVector3D(unittest.TestCase):
    def test_init(self):
        v = entities.Vector3D( (1.0,2.0,3.0) )
       
        self.assertAlmostEqual(v.x, 1.0)
        self.assertAlmostEqual(v.y, 2.0)
        self.assertAlmostEqual(v.z, 3.0)

        self.assertAlmostEqual(v[0], 1.0)
        self.assertAlmostEqual(v[1], 2.0)
        self.assertAlmostEqual(v[2], 3.0)

        self.assertAlmostEqual(v.norm, math.sqrt(14.0))
    def test_from_vector(self):
        v = 
def alltests():
    return unittest.TestLoader().loadTestsFromTestCase(TestVector3D)

if __name__ == '__main__':
    unittest.main()
    
