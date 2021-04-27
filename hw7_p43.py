from dirichlet import Dirichlet,Graph

#SOL for 42

n = {'a': 'bde',
     'b': 'acf',
     'c': 'bdg',
     'd': 'ach',
     'e': 'afh',
     'f': 'bge',
     'g': 'cfh',
     'h': 'deg'}
b = {'a' : 1,
    'b' : 0}
v = 'abcdefgh'

g = Graph(v,n,b)

print("P(x) = \n" + str(Dirichlet(g)))