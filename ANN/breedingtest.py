import numpy as np
from numpy import *

random.seed(1)

bred = 0.001*(np.random.randint(-1000, 1000, size=(1, 6, 6)))
print bred
bred = 0.001*(np.random.randint(-1000, 1000, size=(1, 6, 6)))
print bred

def join(p1,p2):
	temp=[]
	for i in xrange(len(p1)):
		temp.append(list(ravel(p1[i])))
	for i in xrange(len(p2)):
		temp.append(list(ravel(p2[i])))
	return mat(temp)

child1 = join(bred[0][0:3],bred[1][3:6])
child2 = join(bred[1][0:3],bred[0][3:6])

new = []
new.append(child1)
new.append(child2)
print new[1]
