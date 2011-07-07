# @author Stefano Borini
import unittest
import math

from geometry import measure
from geometry import entities

class TestMeasure(unittest.TestCase): 
    def test_norm_BoundVector3D(self):
        self.assertEqual( measure.norm(entities.BoundVector3D( (1.0,2.0,3.0), (2.0, 3.0, 4.0) )), math.sqrt(3.0))

    def test_norm_Vector3D(self):
        self.assertEqual( measure.norm(entities.Vector3D( (1.0, 2.0, 3.0) )), math.sqrt(14.0))

    def test_distance(self): 
        p1 = entities.Point3D( 1.0,2.0,3.0 )
        p2 = entities.Point3D( 2.0,2.0,3.0 )
        self.assertEqual(measure.distance(p1, p2), 1.0)

    def test_distance_2(self): 
        p1 = ( 1.0,2.0,3.0 )
        p2 = ( 2.0,2.0,3.0 )
        self.assertEqual(measure.distance(p1, p2), 1.0)

    def test_angle(self): 
        p1 = entities.Point3D( 1.0,0.0,0.0 )
        p2 = entities.Point3D( 0.0,0.0,0.0 )
        p3 = entities.Point3D( 0.0,1.0,0.0 )
        self.assertEqual(measure.angle(p1, p2, p3), math.pi/2.0 )

    def test_angle_2(self): 
        p1 = ( 1.0,0.0,0.0 )
        p2 = ( 0.0,0.0,0.0 )
        p3 = ( 0.0,1.0,0.0 )
        self.assertEqual(measure.angle(p1, p2, p3), math.pi/2.0 )

    def test_dihedral(self):
        p1 = entities.Point3D( 1.0,0.0,0.0 )
        p2 = entities.Point3D( 0.0,0.0,0.0 )
        p3 = entities.Point3D( 0.0,1.0,0.0 )
        p4 = entities.Point3D( 1.0,1.0,0.0 )
        p5 = entities.Point3D( -1.0,1.0,0.0 )
        self.assertEqual(measure.angle(p1, p2, p3, p4), 0.0 )
        self.assertEqual(measure.angle(p1, p2, p3, p5), math.pi )

    def test_dihedral_2(self):
        p1 = ( 1.0,0.0,0.0 )
        p2 = ( 0.0,0.0,0.0 )
        p3 = ( 0.0,1.0,0.0 )
        p4 = ( 1.0,1.0,0.0 )
        p5 = ( -1.0,1.0,0.0 )
        self.assertEqual(measure.angle(p1, p2, p3, p4), 0.0 )
        self.assertEqual(measure.angle(p1, p2, p3, p5), math.pi )
     
def alltests():
    return unittest.TestLoader().loadTestsFromTestCase(TestMeasure)

if __name__ == '__main__':
    unittest.main()
    
