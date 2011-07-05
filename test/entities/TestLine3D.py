# @author Stefano Borini
import os; import sys; script_path=sys.path[0]; sys.path.append(os.path.join(script_path, "../../../"));
import unittest

import geometry 

class TestLine3D(unittest.TestCase):
    def testInit(self):
        l = geometry.Line3D.through_points( ( 0.0, 0.0, 0.0), (1.0,2.0,3.0) )

        self.assertEqual(l.value(1.0).__class__, geometry.Point3D)
        self.assertEqual(l.value(1.0)[0], 1.0)
        self.assertEqual(l.value(1.0)[1], 2.0)
        self.assertEqual(l.value(1.0)[2], 3.0)
        
        self.assertEqual(l.value(0.5)[0], 0.5)
        self.assertEqual(l.value(0.5)[1], 1.0)
        self.assertEqual(l.value(0.5)[2], 1.5)

        v = geometry.BoundVector3D.from_points( ( 0.0, 0.0, 0.0), (1.0,2.0,3.0) )
        l = geometry.Line3D.from_vector(v)

        self.assertEqual(l.value(1.0)[0], 1.0)
        self.assertEqual(l.value(1.0)[1], 2.0)
        self.assertEqual(l.value(1.0)[2], 3.0)
        
        self.assertEqual(l.value(0.5)[0], 0.5)
        self.assertEqual(l.value(0.5)[1], 1.0)
        self.assertEqual(l.value(0.5)[2], 1.5)

        v = geometry.Vector3D.from_point( (1.0,2.0,3.0) )
        l = geometry.Line3D.from_vector(v)

        self.assertEqual(l.value(1.0)[0], 1.0)
        self.assertEqual(l.value(1.0)[1], 2.0)
        self.assertEqual(l.value(1.0)[2], 3.0)
        
        self.assertEqual(l.value(0.0)[0], 0.0)
        self.assertEqual(l.value(0.0)[1], 0.0)
        self.assertEqual(l.value(0.0)[2], 0.0)
    
    

if __name__ == '__main__':
    unittest.main()
    
