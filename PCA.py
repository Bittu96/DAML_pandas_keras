import numpy as np
import pandas as pd
import scipy.stats  as stats
import matplotlib.pyplot as plt
import math
np.random.seed(6)

population_heights = stats.poisson.rvs(loc=3, mu=1, size=1000)
sample_heights = stats.poisson.rvs(loc=3, mu=1, size=30)

print sample_heights
print( population_heights.mean() )
print( sample_heights.mean() )

print stats.ttest_1samp(a= sample_heights , popmean= population_heights.mean())

print stats.t.ppf(q=0.025, df=49) 
print stats.t.ppf(q=0.975, df=49)

print stats.t.cdf(x= -2.5742, df= 49) * 2  

plt.figure(figsize=(12,10))

plt.fill_between(x=np.arange(-4,-2,0.01), 
                 y1= stats.norm.pdf(np.arange(-4,-2,0.01)) ,
                 facecolor='red',
                 alpha=0.7)

plt.fill_between(x=np.arange(-2,2,0.01), 
                 y1= stats.norm.pdf(np.arange(-2,2,0.01)) ,
                 facecolor='blue',
                 alpha=0.1)

plt.fill_between(x=np.arange(2,4,0.01), 
                 y1= stats.norm.pdf(np.arange(2,4,0.01)) ,
                 facecolor='red',
                 alpha=0.7)

plt.grid()
plt.show()
