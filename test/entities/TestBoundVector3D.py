# @author Stefano Borini
import os; import sys; script_path=sys.path[0]; sys.path.append(os.path.join(script_path, "../../../"));
import unittest

from geometry import entities
import math

class TestBoundVector3D(unittest.TestCase):
    def test_init(self):
        v = entities.BoundVector3D.from_points( (0.0, 0.0, 0.0), (1.0,2.0,3.0) )
       
        self.assertEqual(v.start.__class__, entities.Point3D)
        self.assertEqual(v.start[0], 0.0)
        self.assertEqual(v.start[1], 0.0)
        self.assertEqual(v.start[2], 0.0)

        self.assertEqual(v.end.__class__, entities.Point3D)
        self.assertEqual(v.end[0], 1.0)
        self.assertEqual(v.end[1], 2.0)
        self.assertEqual(v.end[2], 3.0)

    def test_norm(self):
        v = entities.BoundVector3D.from_points( (1.0, 1.0, 1.0), (2.0,3.0,4.0) )
       
        self.assertAlmostEqual(v.norm, math.sqrt(14.0))
   
    def from_vector(self):
        v = Vector3D(1.0, 2.0, 3.0)
        bv = entities.BoundVector3D.from_vector( v ) 

        self.assertEqual(v.start[0], 0.0)
        self.assertEqual(v.start[1], 0.0)
        self.assertEqual(v.start[2], 0.0)

        self.assertEqual(v.end[0], 1.0)
        self.assertEqual(v.end[1], 2.0)
        self.assertEqual(v.end[2], 3.0)

        origin = (3.0, 2.0, 1.0)
        bv = entities.BoundVector3D.from_vector( v, o ) 

        self.assertEqual(v.start[0], 3.0)
        self.assertEqual(v.start[1], 2.0)
        self.assertEqual(v.start[2], 1.0)

        self.assertEqual(v.end[0], 4.0)
        self.assertEqual(v.end[1], 4.0)
        self.assertEqual(v.end[2], 4.0)

def alltests():
    return unittest.TestLoader().loadTestsFromTestCase(TestBoundVector3D)

if __name__ == '__main__':
    unittest.main()
    
