from numpy import *
import pandas as pd

random.seed(1)

def sigm(x, deriv=False):
	if(deriv==True):
		return (x*(1-x))
	return 1/(1+ exp(-x))

l = 1

series = 1.0000000*random.randint(1.00,10.00,10)
series_norm = (series- series.min()) / (series.max()- series.min())
print series
print series_norm
series = series_norm
xi= []

i=0
n = 4

while i<(len(series)-n):
	xi.append(series[i:i+n])
	i+=1

x = array(mat(xi))
print x

y = array((mat(series[n:len(series)])).T)
print y

wt0 = random.random((4,10)) 
wt1 = random.random((10,1))

print wt0

for j in xrange(100000):
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
l2_denorm = (l2*(l2.max() - l2.min())) + l2.min()
print l2_denorm
print wt0