from numpy import *
import matplotlib.pyplot as plt

x = mat([
[3.5, 4.25],
[4.4, 3],
[4, 4],
[4.5, 1.75],
[4.9, 4.5],
[5, 4],
[5.5, 3.5],
[5.5, 3.5],
[0.5, 1.5],
[1, 2.5],
[1.25, 0.5],
[1.5, 1.5],
[2, 2],
[2.5, 0.75],
[4, 2],
[2, 3],
[3, 2],
[5, 3]
])
print x

y = mat([
[1,1,1,1,1,1,1,1,1,
-1,-1,-1,-1,-1,-1,
1,-1,-1]
]).T
print y

lamda = mat([
[0.0271,0.2162,0,0.9928,0,0,0,0,0,0,0,0,0.9928,0.2434,1,1,1,1]
]).T
print lamda

mu = 1-lamda
print mu

w_ = mat([[0.834],[0.333]])
print w_

b = y - (w_.T * x.T).T
print b
print 'bavg :',b.mean()

plt.grid()
plt.show()