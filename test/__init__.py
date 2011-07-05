import unittest
from . import entities

def alltests():
    return unittest.TestSuite([
        entities.alltests(),
    ])

def run():
    return alltests()
    
