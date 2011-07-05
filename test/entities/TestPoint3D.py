# @author Stefano Borini
import os; import sys; script_path=sys.path[0]; sys.path.append(os.path.join(script_path, "../../../"));
import unittest

from geometry import entities
import types


class TestPoint3D(unittest.TestCase):
    def test_init(self):
        v = entities.Point3D(1.0,2.0,3.0)
       
        self.assertAlmostEqual(v.x, 1.0)
        self.assertAlmostEqual(v.y, 2.0)
        self.assertAlmostEqual(v.z, 3.0)

        self.assertAlmostEqual(v[0], 1.0)
        self.assertAlmostEqual(v[1], 2.0)
        self.assertAlmostEqual(v[2], 3.0)

        self.assertEqual(type(v.xyz), types.TupleType)
        self.assertEqual(len(v.xyz), 3)

        self.assertRaises(ValueError, entities.Point3D, (2,3))
        self.assertRaises(TypeError, entities.Point3D, 2,3)

        self.assertRaises(ValueError, entities.Point3D, "foo", "bar", "baz")

def alltests():
    return unittest.TestLoader().loadTestsFromTestCase(TestPoint3D)

if __name__ == '__main__':
    unittest.main()
    
