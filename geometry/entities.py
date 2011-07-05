import math 

from . import _Gohlke_transformations

class Point3D(object):
    """Defines a point in 3D space"""
    def __init__(self, *args):
        """Initializes a point either from three values, or from a sequence of three values"""
        if len(args) == 3:
            self._xyz = tuple([float(x) for x in args])
        elif len(args) == 1:
            if isinstance(args[0],Point3D):
                self._xyz = tuple([float(x) for x in args[0].xyz])
            else:
                self._xyz = tuple([float(x) for x in args[0]])
        else:
            raise TypeError("Invalid number of arguments")
        if len(self._xyz) != 3:
            raise ValueError("Invalid number of values")
    @property
    def xyz(self):
        """Returns the coordinate of the point in 3D space"""
        return self._xyz
    @property
    def x(self):
        """Returns the x component of the point"""
        return self._xyz[0]
    @property
    def y(self):
        """Returns the x component of the point"""
        return self._xyz[1]
    @property
    def z(self):
        """Returns the x component of the point"""
        return self._xyz[2]
    def __getitem__(self, key):
        """Returns the component of the point in progressive order"""
        return self._xyz[key]
    def __repr__(self):
        return "Point3D(%g,%g,%g)" % self._xyz

class BoundVector3D(object):
    """Represent a vector with a starting and ending point. Different from a Vector3D
    in the fact that a Vector3D is defined by only one point (the other being implicitly 
    the origin)"""
    def __init__(self, start, end):
        """Initializes the BoundVector from two 3D points"""
        if isinstance(start, Point3D):
            self._start = Point3D(start.xyz)
        else:
            self._start = Point3D(start)
        
        if isinstance(end, Point3D):
            self._end = Point3D(end.xyz)
        else:
            self._end = Point3D(end)
    @classmethod
    def from_points(cls, start, end):
        """Alternative constructor, similar to the standard one"""
        return cls(start, end)
    @classmethod
    def from_vector(cls, vector, origin=None):
        """Alternative constructor, creates a bound vector from a Vector3D.
        If origin is specified """
        raise NotImplementedError
    @property
    def start(self):
        return self._start
    @property
    def end(self):
         return self._end
    @property
    def norm(self):
        return math.sqrt(  pow((self._end.x-self._start.x),2)
                          +pow((self._end.y-self._start.y),2)
                          +pow((self._end.z-self._start.z),2)
                        )

class Vector3D(object):
    """Defines a free vector"""
    @classmethod
    def from_vector(cls, vector):
        if type(vector) == BoundVector3D:
            return cls( (vector.end.x - vector.start.x,
                         vector.end.y - vector.start.y,
                         vector.end.z - vector.start.z)
                      )
        elif type(vector) == Vector3D:
            return cls(vector.xyz)
    def __init__(self, components):
        self._end = Point3D(components)

    @property
    def xyz(self):
        return self._end.xyz
    @property
    def x(self):
        return self._end.x
    @property
    def y(self):
        return self._end.y
    @property
    def z(self):
        return self._end.z
    @property
    def norm(self):
        return math.sqrt(pow((self._end.x),2)+pow((self._end.y),2)+pow((self._end.z),2))
    def __getitem__(self, key):
        return self._end[key]
    def __mul__(self, value):
        return Vector3D( (self.x*value, self.y*value, self.z*value))
    def __div__(self, value):
        return Vector3D( (self.x/value, self.y/value, self.z/value))
    def __add__(self, other):
        return Vector3D( (self.x + other.x, self.y + other.y, self.z + other.z))
    def __sub__(self, other):
        return Vector3D( (self.x - other.x, self.y - other.y, self.z - other.z))

class Line3D(object):
    @classmethod
    def through_points(cls, p1, p2):
        return cls(BoundVector3D(p1, p2))
    @classmethod
    def from_vector(cls, vector):
        if isinstance(vector, BoundVector3D):
            return cls(vector)
        else:
            return cls(BoundVector3D(Point3D( 0.0,0.0,0.0 ), Point3D(vector.xyz)))
    def __init__(self,bv):
        self._bound_vector = bv
    def value(self,t):
         return Point3D( self._bound_vector.end.coordinates() * t + self._bound_vector.start().coordinates() * (1.0-t))

class Quaternion(object):
    @classmethod
    def from_Vector3D(cls, axis, angle):
        w = math.cos(angle/2.0)
        s = math.sin(angle/2.0)
        x = float(axis[0])*s
        y = float(axis[1])*s
        z = float(axis[2])*s
        return cls(axis=axis, angle=angle, components=[x,y,z,w])
         
    def __init__(self, **args): 
        self._angle = args.get("angle", None)
        self._axis = args.get("axis", None)
        self._components = args.get("components", None)

    def x(self): 
        return self._components[0]
    def y(self): 
        return self._components[1]
    def z(self): 
        return self._components[2]
    def w(self): 
        return self._components[3]
    def axis(self):
        return self._axis
    def angle(self):
        return self._angle
    def __getitem__(self, key):
        return self._components[key]
    def toRotationMatrix(self): 
        return _Gohlke_transformations.quaternion_matrix(self._components)
       
class Sphere(object):
    def __init__(self, center, radius):
        self.center = Point3D(center)
    @property
    def center(self):
        pass
    @property
    def radius(self):
        pass
    @property
    def volume(self):
        return 4.0/3.0 * math.pi * math.pow(self._radius,3)
    @property
    def area(self):
        return 4.0 * math.pi * math.pow(self._radius, 2)
    @classmethod
    def from_three_points(cls, p1,p2,p3):
        pass
    def from_center_radius(cls, center, radius):
        return cls(center, radius)
    def from_vector(cls, vector):
        if isinstance(vector, BoundVector3D):
            return cls(vector.start, vector.norm)
        elif isinstance(vector, Vector3D):
            return cls( (0.0, 0.0, 0.0), vector.norm)
        else:
            raise TypeError("Invalid vector")
    @property
    def bounding_box(self):
        raise NotImplementedError 

class Plane3D(object):
    def __init__(self, point, normal):
        self._point = point
        self._normal = normal
    def from_three_points(cls, p1,p2,p3):
        pass
    def from_line_point(cls, line, point):
        pass
    def from_point_normal(cls, point,normal):
        pass
    def from_bound_normal(cls, normal):
        pass

class Segment3D(object):
    pass

class CatmullRomSpline(object):
    pass

class Disk3D(object):
    def __init__(self, center, radius, normal):
        pass
    pass


class Circle3D(object):
    pass

class Line2D(object):
    pass

class Point2D(object):
    pass

class Disk2D(object):
    pass

class Circle2D(object):
    pass

class Ellipse2D(object):
    pass


xAxis3D = Vector3D( (1.0, 0.0, 0.0) )
yAxis3D = Vector3D( (0.0, 1.0, 0.0) )
zAxis3D = Vector3D( (0.0, 0.0, 1.0) )
xPlane3D = None
yPlane3D = None
zPlane3D = None
origin3D = Point3D( (0.0, 0.0, 0.0) )
