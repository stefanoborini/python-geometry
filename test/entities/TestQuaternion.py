# @author Stefano Borini
import os; import sys; script_path=sys.path[0]; sys.path.append(os.path.join(script_path, "../../../"));
import unittest

import math

class TestQuaternion(unittest.TestCase):
    def test_init(self): # fold>>
        q = entities.Quaternion.from_vector( entities.Vector3D(1.0,2.0,3.0), math.pi/4.0 )
        
        self.assertAlmostEqual(q.w, math.cos(math.pi/8.0))
        self.assertAlmostEqual(q.x, 1.0*math.sin(math.pi/8.0))
        self.assertAlmostEqual(q.y, 2.0*math.sin(math.pi/8.0))
        self.assertAlmostEqual(q.z, 3.0*math.sin(math.pi/8.0))

    def test_to_rotation_matrix(self): 
        q = entities.Quaternion.from_vector(entities.Vector3D(1.0,0.0,0.0) , 0.0615)
        m = transform.Rotation.from_quaternion(q)
        self.assertAlmostEqual(m[0][0], 1.0)
        self.assertAlmostEqual(m[0][1], 0.0)
        self.assertAlmostEqual(m[0][2], 0.0)
        self.assertAlmostEqual(m[1][0], 0.0)
        self.assertAlmostEqual(m[1][1], math.cos(0.0615))
        self.assertAlmostEqual(m[1][2], -math.sin(0.0615))
        self.assertAlmostEqual(m[2][0], 0.0)
        self.assertAlmostEqual(m[2][1], math.sin(0.0615))
        self.assertAlmostEqual(m[2][2], math.cos(0.0615))

        q = entities.Quaternion.from_vector(entities.Vector3D(1.0,0.0,0.0),-0.0615)
        m = transform.Rotation.from_quaternion(q)
        self.assertAlmostEqual(m[0][0], 1.0)
        self.assertAlmostEqual(m[0][1], 0.0)
        self.assertAlmostEqual(m[0][2], 0.0)
        self.assertAlmostEqual(m[1][0], 0.0)
        self.assertAlmostEqual(m[1][1], math.cos(-0.0615))
        self.assertAlmostEqual(m[1][2], -math.sin(-0.0615))
        self.assertAlmostEqual(m[2][0], 0.0)
        self.assertAlmostEqual(m[2][1], math.sin(-0.0615))
        self.assertAlmostEqual(m[2][2], math.cos(-0.0615))

if __name__ == '__main__':
    unittest.main()
    
