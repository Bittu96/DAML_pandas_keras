from numpy import *

def sigm(x, deriv=False):
	if(deriv==True):
		return (x*(1-x))
	return 1/(1+ exp(-x))

l = 1

x = array([
[0,0,1,1],
[1,0,1,0]
])

y = array([
[0,1],
[1,0]
])

random.seed(1)

wt0 = random.random((4,10)) 
wt1 = random.random((10,2))

print wt0
print 'split: \n',wt0[0:2]


for j in xrange(60000):

	l0 = x
	l1 = sigm(dot(l0, wt0))
	l2 = sigm(dot(l1, wt1))

	l2_error = y - l2
	if (j % 10000) == 0:
		print 'Error:' + str(mean(abs(l2_error)))

	l2_delta = l2_error*sigm(l2, deriv=True)
	l1_error = l2_delta.dot(wt1.T)
	l1_delta = l1_error*sigm(l1, deriv=True)

	wt1 += l*l1.T.dot(l2_delta)
	wt0 += l*l0.T.dot(l1_delta)

print 'After training'	
print l2
print wt0

