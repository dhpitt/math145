# David Pitt
# laplacianh 145 - HW7

import numpy as np
import scipy.linalg as linalg
from dirichlet import Graph, Dirichlet
from pprint import pprint

def iterative_Dirichlet(graph,num_iter):
    #Problem 44, HW7
    dim = len(graph.verts)

    laplacian = np.zeros([dim,dim])

    # Set f_0
    fVec = np.zeros([dim,1])
    for i in range(len(graph.verts)):
        if graph.verts[i] in graph.bvals:
            fVec[i][0] = graph.bvals[graph.verts[i]]
        else:
            fVec[i][0] = 0
    
    # Create the graph's Laplacian transformation
    for i in range(len(graph.verts)):
        node1 = graph.verts[i]
        for j in range(len(graph.verts)):
            node2 = graph.verts[j]
            if node2 in list(graph.neighbors[node1]) and node1 not in graph.bvals:
                laplacian[i][j] = -1/len(graph.neighbors[node1])
            elif node1 == node2:
                laplacian[i][j] = 1
            else:
                laplacian[i][j] = 0
    #pprint(laplacian)
    newF = fVec
    for i in range(num_iter):
        lapF = laplacian.dot(newF)
        newF = lapF - newF

        # The field is always equal to the starting
        # boundary values on the boundary. 
        for i in range(len(graph.verts)):
            if graph.verts[i] in graph.bvals:
                newF[i][0] = graph.bvals[graph.verts[i]]

    print("Scalar field f(x) after {} iterations: ".format(num_iter))
    for i in range(dim):
        print(str(graph.verts[i]) + " = " + str(newF[i]))
    return newF         

gn1 = {'a': 'bh',
     'b': 'aci',
     'c': 'bdj',
     'd': 'cek',
     'e': 'dfl',
     'f': 'egm',
     'g': 'fn',
     'h': 'aio',
     'i': 'bhjp',
     'j': 'cikq',
     'k': 'djlr',
     'l': 'ekms',
     'm': 'flnt',
     'n': 'gmu',
     'o': 'hpv',
     'p': 'ioqw',
     'q': 'jprx',
     'r': 'kqsy',
     's': 'lrtz',
     't': 'musA',
     'u': 'tnB',
     'v': 'owC',
     'w': 'pvxD',
     'x': 'qwyE',
     'y': 'rxzF',
     'z': 'syAG',
     'A': 'ztBH',
     'B': 'uAI',
     'C': 'vDJ',
     'D': 'wCEK',
     'E': 'xDFL',
     'F': 'yEGM',
     'G': 'zFHN',
     'H': 'AGIO',
     'I': 'BHP',
     'J': 'CKQ',
     'K': 'DJLR',
     'L': 'EKMS',
     'M': 'FLNT',
     'N': 'GMOU',
     'O': 'HNPV',
     'P': 'IOW',
     'Q': 'JR',
     'R': 'QKS',
     'S': 'LRT',
     'T': 'MSU',
     'U': 'NTV',
     'V': 'OVW',
     'W': 'PV'}
    
gverts1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW'
gbound1 = 'abcdefghnouvBCIJPQRSTUVWy'
bvals1 = {}
for character in gbound1:
    if character == 'y':
        bvals1[character] = 1
    else:
        bvals1[character] = 0

graph_1 = Graph(gverts1,gn1,bvals1)

iterative_Dirichlet(graph_1,24)
#print(Dirichlet(graph_1))
