################################################################################
# HW6 CS103 Fall 2019
import turtle
import math 
# I declare that I have completed this assignment completely and entirely
# on my own, without any consultation with others.
# I also declare that I have not used internet resources or physical books
# to help with this assignment, except for non-coding mathematical literature
# to help understand the computational approach to these questions.
# I have read the UAB Academic Honor Code and understand that any breach
# of the Honor Code may result in severe penalties.

# name:
# blazerid:
################################################################################

################################################################################
# will be used by the autograder
def myName (): 
    # PLEASE REPLACE 'Alan Turing' BY YOUR NAME; do not change anything else;
    # for example, leave the single quotes alone as you insert your name
    return 'Alan Turing'
################################################################################

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, second):
        x_d = self.x - second.x
        y_d = self.y - second.y
        return (x_d**2 + y_d**2) **0.5

class Pol (Point): 

    """Pol is a closed polygon in 2-space."""

    def __init__ (self, points):  #am I drawing or could I just do vtx= (0,0),(0,90),(45,90),(90,90), (90,0)
        self.points = points
        
        """Initialize a closed polygon from a list of vertices.
        Params: vtx (list of float 2-tuples) vertices, ordered around the bdry
        """
    
    def __len__(self):
        return(len(self.points))

    def __str__ (self):

        """str method
        Returns: (str) a string representation of the polygon
        """
        return ''  # will complain about 'pass' here: needs a string, not None

    def perimeter (self): 
        
        perimeter = 0
        for i in range(1, len(self.points)):
            pt1 = self.points[i-1]
            pt2 = self.points[i]
            perimeter += pt1.distance(pt2)
            if i+1 == len(self.points):
                perimeter += self.points[-1].distance(self.points[0])
            else:
                continue

        return perimeter
                
        """Sum of the lengths of the sides of the polygon.
        Returns: (float) perimeter
        """

    def avgEdgeLength (self):

        avgLength = 0
        for i in range(1, len(self.points)):
            pt1 = self.points[i-1]
            pt2 = self.points[i]
            avgLength += pt1.distance(pt2)
            if i+1 == len(self.points):
                avgLength += self.points[-1].distance(self.points[0])
            else:
                continue

        return avgLength/len(self.points)

        """
        Returns: (float) average edge length
        """

    def angle (self, i): #considering regular polygon

        angle = 180*(len(self.points)-2)/len(self.points) 
        return angle       

        """
        Params: i (int): vertex index (0 = first vertex) 
        Returns: (float) angle, in degrees, at vertex i
        """

    def isSimple (self):                                        # optional bonus

        """Test for simplicity.
        A polygon is simple if it has no self-intersections.
        That is, non-neighbouring edges do not intersect.
        Returns: (bool) is this polygon simple?
        """
        pass

    def isConvex (self):                                        # optional bonus

        """Test for convexity.

        A set S is convex if A, B in S implies the line segment AB is in S.
        But can you make this computational?
        Hint: the cross product is your friend.

        Returns (bool) is this polygon convex?
        """
        pass

class Tri ():

    """Tri is a triangle class."""

    def __init__ (self, A, B, C, rgbA, rgbB, rgbC):
        self.A = A
        self.B = B
        self.C = C
        self.rgbA = rgbA
        self.rgbB = rgbB
        self.rgbC = rgbC
        self.a = math.sqrt(abs(self.B[0]-self.A[0])**2 + abs(self.B[1]-self.A[1])**2)
        self.b = math.sqrt(abs(self.C[0]-self.B[0])**2 + abs(self.C[1]-self.B[1])**2)
        self.c = math.sqrt(abs(self.A[0]-self.C[0])**2 + abs(self.A[1]-self.C[1])**2)
        self.angA = math.atan((self.B[1]-self.A[1])/(self.B[0]-self.A[0]))
        self.angB = math.atan((self.C[1]-self.B[1])/(self.C[0]-self.B[0]))
        self.angC = math.atan((self.A[1]-self.C[1])/(self.A[0]-self.C[0]))

        """
        Params:
            A,B,C (float 2-tuples): vertices of the triangle ABC
            rgbA, rgbB, rgbC (int 3-tuples): RGB colours of the vertices
                     colour range is [0,255]; e.g., 0 <= rgbA[i] <= 255
        """

    def __str__ (self):

        """
        Returns: (str) a string representation of the triangle
        """
        return ''  # will complain about 'pass' here: needs a string, not None

    def getColour (self, i):
        
        if i == 0:
            return self.rgbA
        elif i == 1:
            return self.rgbB
        elif i == 2:
            return self.rgbC

        """
        Params: i (int): vertex index, 0<=i<=2
        Returns: (int 3-tuple) colour of ith vertex
        """

    def isEquilateral (self):

        if self.a == self.b == self.c:
            return True
        else:
            return False    

        """Test for equilateral triangle.
        Params: eps (float): allowable deviation in length
        Returns: (bool) is the triangle equilateral within eps?
                        (difference between min edge and max edge < eps?)
        """

    def signedArea (self):
        
        s = (self.a + self.b + self.c)/2
        area = math.sqrt(s*((s-self.a)*(s-self.b)*(s-self.c)))
        return area

        """
        Returns: (float) signed area of the triangle, +ve iff counterclockwise
        """

    def isCCW (self):
        
        """Counterclockwise orientation.
        ccw iff all (both) turns are left
        Returns: (bool) is the triangle oriented counterclockwise?
        """
        pass
        
    def centroid (self):
        x_centroid = (self.A[0] + self.B[0] + self.C[0])/3
        y_centroid = (self.A[1] + self.B[1] + self.C[1])/3

        return (float("%.2f"%x_centroid), float("%.2f"%y_centroid))
        # optional bonus

        """
        Returns: (float 2-tuple): centroid of the triangle
        """
        

    def circumCenter (self):                                    # optional bonus
        cC_x = (self.A[0]*math.sin(2*self.angA) + self.B[0]*math.sin(2*self.angB) + self.C[0]*math.sin(2*self.angC))/(math.sin(2*self.angA) + math.sin(2*self.angB) + math.sin(2*self.angC))
        cC_y = (self.A[1]*math.sin(2*self.angA) + self.B[1]*math.sin(2*self.angB) + self.C[1]*math.sin(2*self.angC))/(math.sin(2*self.angA) + math.sin(2*self.angB) + math.sin(2*self.angC))        

        return (float("%.2f"%cC_x), float("%.2f"%cC_y))
        """Circumcenter, the center of the circumscribing circle.
        Returns: (float 2-tuple): circumcenter of the triangle
        """

pt1 = Point(0,0)
pt2 = Point(0,4)
pt3 = Point(3,0)
triangle = Pol([pt1,pt2,pt3]) #yes, the class Polygon will be initialized using a list
print(triangle.perimeter())


tri = Tri((2,3),(7,4),(3,5),[1,45,234], [34,45,99], [0,123,245]) 
print(tri.circumCenter())
    
