import unittest
import math

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):         # return string "Vector(x, y, z)"
        return f"Vector({self.x},{self.y},{self.z})"
        
    def __eq__(self, other):    # v == w
        return True if self.x == other.x and self.y == other.y and self.z == other.z else False
    
    def __ne__(self, other):        # v != w
        return not self == other

    def __add__(self, other):    # v + w
        return Vector(self.x + other.x,self.y + other.y,self.z+other.z)
        # Hint: return Vector(...)

    def __sub__(self, other):    # v - w
        return Vector(self.x - other.x,self.y - other.y,self.z - other.z)

    def __mul__(self, other):   # return the dot product (number)
        return self.x*other.x + self.y*other.y + self.z*other.z
    
    def cross(self, other):   # return the cross product (Vector)
        return Vector(self.y*other.z-self.z*other.y,self.z*other.x-self.x*other.z,self.x*other.y-self.y*other.x)
    
    def length(self):    # the length of the vector
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
    
    def __hash__(self):   # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))   # recommended

class TestVector(unittest.TestCase): 
    VA = Vector(0,1,2)
    VB = Vector(-1,2,0)
    VC = Vector(0.5,5,-2)
   
    
    def test_repr(self):
        self.assertEqual(Vector(-1,2,-3).__repr__(),"Vector(-1,2,-3)")  #repr oddaje to co mamy w return danej metody
        self.assertEqual(Vector(1,2,3).__repr__(),"Vector(1,2,3)") 
        self.assertEqual(Vector(0,0,-1).__repr__(),"Vector(0,0,-1)") 
        self.assertEqual(Vector(1,-2,3).__repr__(),"Vector(1,-2,3)") 

        
    def test_eq(self):
        VA = Vector(0,1,2)
        VB = Vector(-1,2,0)
        VC = Vector(0.5,5,-2)
        self.assertTrue(VA.__eq__(VA))
        self.assertTrue(VB.__eq__(VB))
        self.assertTrue(VC.__eq__(VC))
        self.assertFalse(VC.__eq__(VB))
        self.assertFalse(VC.__eq__(VA))

        
    def test_ne(self):
        VA = Vector(0,1,2)
        VB = Vector(-1,2,0)
        VC = Vector(0.5,5,-2)
        self.assertTrue(VA.__ne__(VB))
        self.assertTrue(VC.__ne__(VB))
        self.assertFalse(VA.__ne__(VA))
         #self.assertFalse(VC == VB)
        
    def test_add(self):
        VA = Vector(0,1,2)
        VB = Vector(-1,2,0)
        VC = Vector(0.5,5,-2)
        self.assertEqual(VA.__add__(VB),Vector(-1,3,2))
        self.assertEqual(VC.__add__(VB),Vector(-0.5,7,-2))
        self.assertEqual(VA.__add__(VC),Vector(0.5,6,0))

        
    def test_sub(self):
        VA = Vector(0,1,2)
        VB = Vector(-1,2,0)
        VC = Vector(0.5,5,-2)
        self.assertEqual(VA.__sub__(VC), Vector(-0.5,-4,4)) 
        self.assertEqual(VA.__sub__(VB), Vector(1,-1,2))
        self.assertEqual(VB.__sub__(VC), Vector(-1.5,-3,2))
        
    def test_mul(self):
        VA = Vector(0,1,2)
        VB = Vector(-1,2,0)
        VC = Vector(0.5,5,-2)
        self.assertEqual(VA.__mul__(VB),2)
        self.assertEqual(VB.__mul__(VC),9.5)
        self.assertEqual(VA.__mul__(VC),1)
        
    def test_cross(self):
        VA = Vector(0,1,2)
        VB = Vector(-1,2,0)
        VC = Vector(0.5,5,-2)
        self.assertEqual(VA.cross(VB),Vector(-4,-2,1)) 
        self.assertEqual(VA.cross(VC),Vector(-12,1.0,-0.5)) 
        self.assertEqual(VC.cross(VB),Vector(4,2.0,6.0)) 
        
    def test_length(self):
        VA = Vector(0,1,2)
        VB = Vector(-1,2,0)
        VC = Vector(0.5,5,-2)
        self.assertEqual(VC.length(), 5.408326913195984)
        self.assertEqual(VB.length(), 2.23606797749979)
        self.assertEqual(VA.length(), 2.23606797749979)


if __name__ == '__main__':
    unittest.main()