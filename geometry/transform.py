from geometry import entities
import math

def normalize(entity): 
    """Returns a new entity, normalized to euclidean norm == 1"""
    if isinstance(entity, entities.Vector3D):
        arr = entity.components()
        return entities.Vector3D( (arr / math.sqrt(numpy.dot(arr, arr))))
    elif isinstance(vector,entities.BoundVector3D):
        arr_start = vector.start().coordinates()
        arr_end = vector.end().coordinates()
        arr_end-arr_start

def rotate(entity, axis, angle):
    q = entities.Quaternion.fromVector3D(axis, angle)
    m = numpy.array(q.toRotationMatrix())
    arr = numpy.array([ entity[0], entity[1], entity[2], 1.0 ])
    rotated = numpy.dot(m, arr)
    if type(entity) == entities.Vector3D:
        return entities.Vector3D( rotated )
    elif type(entity) == entities.Point3D:
        return entities.Point3D( rotated )

    raise TypeError("Unrecognized type") 

def mirror(entity, plane):
    raise NotImplementedError

def translate(entity, vector):
    raise NotImplementedError

def project(entity1, entity2):
    raise NotImplementedError

