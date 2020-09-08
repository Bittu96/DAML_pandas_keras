import math
from math import *
import numpy as np
from numpy import *
import scipy.stats  as stats
import matplotlib.pyplot as plt

#population_heights = stats.poisson.rvs(loc=0, mu=5, size=10)
#print population_heights,population_heights.mean()
muo = 5
alpha = 0.01
tail_cor = 0.5
sample_heights = array([4.8,5.2,4.8,4.9,5.0])
sigmax_= sample_heights.std()/sqrt(len(sample_heights))

print 'sample          :',sample_heights
print 'population mean :',muo  
print 'sample mean     :',sample_heights.mean()
print 'sample std      :',sample_heights.std() 
print 'sample stdx-    :',sigmax_

z = -(sample_heights.mean() - muo)/sigmax_
print 'sample z        :',z

Z = sqrt( -2*log(alpha*tail_cor*sqrt(2*pi)) )
print "Z               :",Z

#print stats.ttest_1samp(a= sample_heights , popmean= population_heights.mean())
#print stats.t.cdf(x= -2.5742, df= 49) * 2 

#Z1 = stats.t.ppf(q = alpha*tail_cor  , df=len(sample_heights) - 1)
#Z2 = stats.t.ppf(q = 1-alpha*tail_cor, df=len(sample_heights) - 1)
Z1 = -abs(Z)
Z2 =  abs(Z)
print 'Z1 :',Z1,'Z2 :',Z2

normalLim = 3.5
plt.fill_between(x=np.arange(-normalLim,Z1,0.01), 
                 y1= stats.norm.pdf(np.arange(-normalLim,Z1,0.01)) ,
                 facecolor='red',
                 alpha=0.9)

plt.fill_between(x=np.arange(Z1,Z2,0.01), 
                 y1= stats.norm.pdf(np.arange(Z1,Z2,0.01)) ,
                 facecolor='blue',
                 alpha=0.5)

plt.fill_between(x=np.arange(Z2,normalLim,0.01), 
                 y1= stats.norm.pdf(np.arange(Z2,normalLim,0.01)) ,
                 facecolor='red',
                 alpha=0.9)

if (z < Z2) and (z > Z1) == True:
	print '--REJECTED-- not the best sample'
else:
	print 'best sample'

plt.plot(z,0,'ro',markersize = 2)
line, = plt.plot([z ,z], [0.4,0], 'red', lw=0.5)
plt.title("Null's Hypothesis")
plt.xlabel("Z")
plt.ylabel("alpha")
plt.grid()
plt.show()