# David Pitt
# Apr 11, 2021
# Solves the Dirichlet problem for finite graphs
# HW6

import numpy as np
import scipy.linalg as linalg

class Graph:
    def __init__(self,verts,neighbors,bvals):
        self.neighbors = neighbors
        self.bvals = bvals
        self.verts = list(verts)
    def __str__(self):
        return('Neighborhoods: ' + str(self.neighbors) + '\n' + 'Boundary vertices: ' + str(self.bvals) + '\n')

def Dirichlet(graph):
    # Takes a graph G with a list of boundary vertices
    # and solves the Dirichlet problem for a scalar field f.
    dim = len(graph.verts)
    Mat = np.zeros([dim,dim])
    solVec = np.zeros([dim,1])
    for i in range(len(graph.verts)):
        node1 = graph.verts[i]
        for j in range(len(graph.verts)):
            node2 = graph.verts[j]
            if node2 in list(graph.neighbors[node1]) and node1 not in graph.bvals:
                Mat[i][j] = -1/len(graph.neighbors[node1])
            elif node1 == node2:
                Mat[i][j] = 1
            else:
                Mat[i][j] = 0
    for i in range(len(graph.verts)):
        if graph.verts[i] in graph.bvals:
            solVec[i][0] = graph.bvals[graph.verts[i]]
        else:
            solVec[i][0] = 0
    
    vals = linalg.solve(Mat,solVec)
    solution_Field = {}
    for i in range(len(vals)):
        solution_Field[graph.verts[i]] = vals[i]
    #return Mat,solution_Field
    return vals

'''
# SOL for 35 ii)
A = np.array([[1,-1/3,-1/3,0,0,0,0,0,0],[-1/3,1,0,-1/3,0,0,-1/3,0,0],[-1/4,0,1,-1/4,-1/4,-1/4,0,0,0],[0,-1/4,-1/4,1,0,0,0,-1/4,-1/4],[0,0,-1/2,0,1,0,0,0,-1/2],[0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,1]])
#print(A.shape)

delta_F = np.zeros([9,1])
delta_F[5] = 0.
delta_F[6] = 3
delta_F[7] = 1
delta_F[8] = 2#

#print(delta_F)
#print(linalg.solve(A,delta_F))
'''

# SOL for 37
gn1 = {'a': 'bf',
     'b': 'acs',
     'c': 'bdg',
     'd': 'ceh',
     'e': 'di',
     'f': 'ajs',
     'g': 'cslh',
     'h': 'dgim',
     'i': 'eht',
     'j': 'fkn',
     'k': 'sjlo',
     'l': 'gkmp',
     'm': 'hltq',
     'n': 'jo',
     'o': 'knp',
     'p': 'loq',
     'q': 'mpr',
     'r': 'qt',
     's': 'bfgk',
     't': 'imr'}
    
gverts1 = 'abcdefghijklmnopqrst'
gbound1 = 'st'
bvals1 = {'s' : 0,
         't': 1}

graph_1 = Graph(gverts1,gn1,bvals1)

print(graph_1)

print("R(x) = \n" + str(Dirichlet(graph_1)))
