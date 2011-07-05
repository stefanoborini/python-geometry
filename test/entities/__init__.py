# @author Stefano Borini
import unittest

from . import TestPoint3D
from . import TestVector3D
from . import TestBoundVector3D

def alltests():
    return unittest.TestSuite([
        TestPoint3D.alltests(),
        TestBoundVector3D.alltests(),
        TestVector3D.alltests()
    ])
    
