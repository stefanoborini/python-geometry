# @author Stefano Borini
import unittest
import numpy
import math

from geometry import transform
from geometry import measure
from geometry import entities

class TestTransform(unittest.TestCase): 
    def test_normalize(self): 
        p1 = transform.normalize(geometry.Vector3D( (1.0,2.0,3.0) ))
        self.assertEqual(measure.norm(p1), 1.0)
    def test_rotate(self):
        v = entities.Vector3D( (2.0,0.0,0.0) )
        axis = entities.Vector3D( (1.0,0.0,0.0) )
        rotated = transform.rotate(v, axis, math.pi/4.0)

        self.assertAlmostEqual(rotated.x, 2.0)
        self.assertAlmostEqual(rotated.y, 0.0)
        self.assertAlmostEqual(rotated.z, 0.0)

        v = entities.Vector3D( (0.0,2.0,0.0) )
       
        rotated = transform.rotate(v, axis, math.pi/4.0)

        self.assertAlmostEqual(rotated.x, 0.0)
        self.assertAlmostEqual(rotated.y, 2.0/math.sqrt(2.0))
        self.assertAlmostEqual(rotated.z, 2.0/math.sqrt(2.0))

        rotated = transform.rotate(v, axis, -math.pi/4.0)

        self.assertAlmostEqual(rotated.x, 0.0)
        self.assertAlmostEqual(rotated.y, 2.0/math.sqrt(2.0))
        self.assertAlmostEqual(rotated.z, -2.0/math.sqrt(2.0))

def alltests():
    return unittest.TestLoader().loadTestsFromTestCase(TestTransform)

if __name__ == '__main__':
    unittest.main()
