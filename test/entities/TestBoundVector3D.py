# @author Stefano Borini
import os; import sys; script_path=sys.path[0]; sys.path.append(os.path.join(script_path, "../../../"));
import unittest

from geometry import entities
import math

class TestBoundVector3D(unittest.TestCase):
    def test_init_from_points_1(self):
        v = entities.BoundVector3D.from_points( (3.0, 2.0, 1.0), (1.0,2.0,3.0) )

        self.assertEqual(v.start.__class__, entities.Point3D)
        self.assertEqual(v.start[0], 3.0)
        self.assertEqual(v.start[1], 2.0)
        self.assertEqual(v.start[2], 1.0)

        self.assertEqual(v.end.__class__, entities.Point3D)
        self.assertEqual(v.end[0], 1.0)
        self.assertEqual(v.end[1], 2.0)
        self.assertEqual(v.end[2], 3.0)

    def test_init_from_points_2(self):
        v = entities.BoundVector3D.from_points( entities.Point3D(3.0, 2.0, 1.0), entities.Point3D(1.0,2.0,3.0) )

        self.assertEqual(v.start.__class__, entities.Point3D)
        self.assertEqual(v.start[0], 3.0)
        self.assertEqual(v.start[1], 2.0)
        self.assertEqual(v.start[2], 1.0)

        self.assertEqual(v.end.__class__, entities.Point3D)
        self.assertEqual(v.end[0], 1.0)
        self.assertEqual(v.end[1], 2.0)
        self.assertEqual(v.end[2], 3.0)

    def test_init_from_vector_1(self):
        bv1 = entities.BoundVector3D.from_points( (3.0, 2.0, 1.0), (1.0,2.0,3.0) )
        bv2 = entities.BoundVector3D.from_vector( bv1 )

        self.assertEqual(v.start.__class__, entities.Point3D)
        self.assertEqual(v.start[0], 3.0)
        self.assertEqual(v.start[1], 2.0)
        self.assertEqual(v.start[2], 1.0)

        self.assertEqual(v.end.__class__, entities.Point3D)
        self.assertEqual(v.end[0], 1.0)
        self.assertEqual(v.end[1], 2.0)
        self.assertEqual(v.end[2], 3.0)

    def test_init_from_vector_2(self):
        v = entities.Vector3D.from_point( 3.0, 2.0, 1.0 )
        bv2 = entities.BoundVector3D.from_vector( v1 )

        self.assertEqual(v.start.__class__, entities.Point3D)
        self.assertEqual(v.start[0], 0.0)
        self.assertEqual(v.start[1], 0.0)
        self.assertEqual(v.start[2], 0.0)

        self.assertEqual(v.end.__class__, entities.Point3D)
        self.assertEqual(v.end[0], 3.0)
        self.assertEqual(v.end[1], 2.0)
        self.assertEqual(v.end[2], 1.0)

    def test_init_from_vector_3(self):
        origin = (3.0, 2.0, 1.0)
        v = entities.Vector3D.from_point( 1.0, 2.0, 3.0 )
        bv = entities.BoundVector3D.from_vector( v, origin ) 

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
    
