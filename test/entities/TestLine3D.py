# @author Stefano Borini
import os; import sys; script_path=sys.path[0]; sys.path.append(os.path.join(script_path, "../../../"));
import unittest

from geometry import entities

class TestLine3D(unittest.TestCase):
    def test_init_through_points_1(self):
        l = entities.Line3D.through_points( ( 0.0, 0.0, 0.0), (1.0,2.0,3.0) )

        self.assertEqual(l.point_at(1.0).__class__, entities.Point3D)
        self.assertEqual(l.point_at(1.0).xyz, (1.0, 2.0, 3.0))
        
        self.assertEqual(l.point_at(1.0).__class__, entities.Point3D)
        self.assertEqual(l.point_at(0.5).xyz, (0.5, 1.0, 1.5))

    def test_init_through_points_2(self):
        l = entities.Line3D.through_points( entities.Point3D( 0.0, 0.0, 0.0), entities.Point3D(1.0,2.0,3.0) )

        self.assertEqual(l.point_at(1.0).__class__, entities.Point3D)
        self.assertEqual(l.point_at(1.0).xyz, (1.0, 2.0, 3.0))
        
        self.assertEqual(l.point_at(0.5).__class__, entities.Point3D)
        self.assertEqual(l.point_at(0.5).xyz, (0.5, 1.0, 1.5))
    
    def test_init_from_vector_1(self):
        bv = entities.BoundVector3D.from_points( ( 1.0, 1.0, 1.0), (3.0,3.0,3.0) )
        l = entities.Line3D.from_vector(bv)

        self.assertEqual(l.point_at(1.0).xyz, (3.0, 3.0, 3.0))
        self.assertEqual(l.point_at(0.0).xyz, (1.0,1.0,1.0))
        self.assertEqual(l.point_at(0.5).xyz, (2.0,2.0,2.0))

        v = entities.Vector3D.from_point( (1.0,2.0,3.0) )
        l = entities.Line3D.from_vector(v)

        self.assertEqual(l.point_at(1.0).xyz, (1.0, 2.0, 3.0))
        self.assertEqual(l.point_at(0.0).xyz, (0.0, 0.0, 0.0))
    

if __name__ == '__main__':
    unittest.main()
    
