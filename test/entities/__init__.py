# @author Stefano Borini
import os; import sys; script_path=sys.path[0]; sys.path.append(os.path.join(script_path, "../../../"));
import unittest

import TestPoint3D
import TestBoundVector3D

def alltests():
    return unittest.TestSuite([
        TestPoint3D.alltests(),
        TestBoundVector3D.alltests(),
        TestVector3D.alltests()
    ])

if __name__ == '__main__':
    unittest.TextTestRunner().run(alltests())
    
