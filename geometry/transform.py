from geometry import entities
import math

def normalized(entity): 
    """Returns a new entity, normalized to euclidean norm == 1"""
    if isinstance(entity, entities.Vector3D):
        arr = entity.components()
        return entities.Vector3D( (arr / math.sqrt(numpy.dot(arr, arr))))
    elif isinstance(vector,entities.BoundVector3D):
        arr_start = vector.start().coordinates()
        arr_end = vector.end().coordinates()
        arr_end-arr_start

def rotated(entity, axis, angle):
    q = entities.Quaternion.from_vector(axis, angle)
    m = numpy.array(q.toRotationMatrix())
    arr = numpy.array([ entity[0], entity[1], entity[2], 1.0 ])
    rotated = numpy.dot(m, arr)
    if type(entity) == entities.Vector3D:
        return entities.Vector3D( rotated )
    elif type(entity) == entities.Point3D:
        return entities.Point3D( rotated )

    raise TypeError("Unrecognized type") 

def mirrored(entity, plane):
    raise NotImplementedError

def translated(entity, vector):
    raise NotImplementedError

def projected(entity1, entity2):
    raise NotImplementedError

