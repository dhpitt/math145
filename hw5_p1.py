# David Pitt, Ryan Martinez, Ryan O'Dowd, Solomon Valore-Caplan
# Mar 24, 2021 # Math 145 HW 2

from math import gcd
from pprint import pprint
# Problem 28
# The Vietoris-Rips Coverage Test

# Import data
data1 = open("robotdata1.txt","r")
data2 = open("robotdata2.txt","r")


def main(data):
    # Create the boundary - doesn't change
    fence = [[x,x+1] for x in range(1,11)]
    fence.append([1,11])

# List the edges
    edgeList = []
    for line in data:
        maxRobot = 0
        newEdge = [int(x) for x in line.split()]
        edgeList.append(newEdge)
        for i in newEdge:
            if i > maxRobot:
                maxRobot = i

    robots = list(range(1,maxRobot+1))
#print(robots)

    edgeList = sorted(edgeList)



# Find robots in range
    rangeList = []
    for i in robots:
        robotsInRange = []
        for edge in edgeList:
            if edge[0] == i:
                robotsInRange.append(edge[1])
            elif edge[1] == i:
                robotsInRange.append(edge[0])
        robotsInRange = sorted(robotsInRange)
        rangeList.append(robotsInRange)
        '''
        for j in range(len(robotsInRange)):
            for k in range(1,len(robotsInRange)-j):
                triangles.append([i,robotsInRange[j],robotsInRange[j+k]])
        '''

# Find all triangles
    triangles = [] #set()

    for i in range(len(robots)):
        for j in range(1,len(robots)-i):
            if robots[i+j] in rangeList[i]:
                for k in rangeList[i+j]:
                    if k in rangeList[i]:
                        tri = [robots[i],robots[i+j],k]
                        tri = sorted(tri)
                        #triangles.add(tuple(tri))
                        if not tuple(tri) in triangles:
                            triangles.append(tuple(tri))
#print(edgeList)
#print(triangles)

# Check to make sure the triangles are all correct

    check = True
    fails = []
    for t in triangles:
        if [t[0],t[1]] not in edgeList:
            fails.append([t[0],t[1]])
            check = False

        elif [t[1],t[2]] not in edgeList:
            fails.append([t[1],t[2]])
            check = False

        elif [t[0],t[2]] not in edgeList:
            fails.append([t[0],t[2]])
            check = False
    #print(check)
    #print(fails)

# Create the coverage matrix
    triangles = list(triangles)

#dim = max(len(edgeList),len(triangles))
#coverageMatrix = np.zeros([len(edgeList),len(triangles)])
    coverageMatrix = [[Rational(0,1) for i in range(len(triangles) + 1)] for j in range(len(edgeList))]


    for i in range(len(triangles)):
        for j in range(len(edgeList)):
            if edgeList[j][0] in triangles[i] and edgeList[j][1] in triangles[i]:
                if edgeList[j][0] == triangles[i][0] and edgeList[j][1] == triangles[i][2]:
                    coverageMatrix[j][i] = Rational(-1, 1)
                else:
                    coverageMatrix[j][i] = Rational(1, 1)
            else:
                coverageMatrix[j][i] = Rational(0, 1)

    #boundary = [0 for i in range(len(edgeList))]
    for i in range(len(edgeList)):
        if edgeList[i] in fence:
            if edgeList[i] != [1,11]:
                #boundary[i] = 1
                coverageMatrix[i][-1] = Rational(1, 1)
            else:
                #boundary[i] = -1
                coverageMatrix[i][-1] = Rational(-1,1)
    else:
        #boundary[i] = 0
        coverageMatrix[i][-1] = Rational(0, 1)

    pivots = rref_Solver(coverageMatrix)
    #mat_print(coverageMatrix)

    necessary_pivots = [pivots[x] for x in range(len(pivots)) if coverageMatrix[x][-1] != Rational(0,1)]
    print("Row rank: " + str(len(pivots)))
    #print("Indices of triangles required: " + str(necessary_pivots))
    used_bots = []
    for t in triangles:
        for i in t:
            if not i in used_bots:
                used_bots.append(i)

    return (consistent(coverageMatrix), sorted([r for r in robots if r not in used_bots]))
    


def mat_print(A):
    for i in A:
        print('\n')
        print(i)


'''
    A is a matrix with an extra column not to be reduced: [A | b]
'''
def rref_Solver(A):

    ''' Scales the ith row in A by k ''' 
    def scale(i, k):
        A[i] = [k * j for j in A[i]]

    ''' Swaps the ith and jth rows of A'''
    def swap(i, j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp

    ''' Adds k times the ith row of A to the jth row of A'''
    def scale_and_add(i, j, k):
        A[j] = [k * A[i][x] + A[j][x] for x in range(len(A[j]))]

    pivots = []
    currow = 0
    for column in range(len(A[0]) - 1): # minus 1 to ignore the last column which holds the 'b' value
        for r in range(currow,len(A)):
            if A[r][column] != Rational(0,1):
                pivots.append(column)
                swap(r, currow)
                scale(currow, Rational(1, 1)/A[currow][column])
                for x in range(0, len(A)):
                    if x != currow:
                        scale_and_add(currow, x, -A[x][column])
                currow += 1
                break
    return pivots


def consistent(matrix):
    for row in matrix:
        if row[-1] != Rational(0,1):
            others = row[:(len(row)-1)]
            if not any(others):
                return False
    return True


class Rational(tuple):

    def __new__(cls, a, b):
        ia = int(a)
        ib = int(b)
        if ia == 0:
            return tuple.__new__(cls, (0, 1))
        if ib == 0:
            raise ZeroDivisionError
        g = gcd(ia,ib)
        return tuple.__new__(cls, (ia//g,ib//g))

    @property
    def a(self):
        return self[0]

    @property
    def b(self):
        return self[1]

    def __eq__(self, other):
        return self.a * other.b == self.b* other.a

    def __bool__(self):
        return not self.__eq__(Rational(0,1))

    __nonzero__=__bool__

    def __add__(self, other):
        return Rational(self.a * other.b + other.a * self.b, self.b * other.b)

    def __neg__(self):
        return Rational(-self.a, self.b)

    def __sub__(self, other):
        return self.__add__(other.__neg__())

    def __mul__(self, other):
        return Rational(self.a * other.a, self.b * other.b)

    def __truediv__(self, other):
        return Rational(self.a * other.b, self.b * other.a)

    def __str__(self):
        return str(self.a) + "/" + str(self.b)

    def __repr__(self):
        return self.__str__()

    def __setattr__(self, *ignored):
        raise NotImplementedError

    def __delattr__(self, *ignored):
        raise NotImplementedError
