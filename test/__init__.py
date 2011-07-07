import unittest
from . import entities
from . import TestTransform
from . import TestMeasure

def alltests():
    return unittest.TestSuite([
        entities.alltests(),
        TestMeasure.alltests(),
        TestTransform.alltests()
    ])

def run():
    return alltests()
    
