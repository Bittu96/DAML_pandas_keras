from numpy import *
from math import * 

input_a = []

def sigm(x, deriv=False):
	if(deriv==True):
		return (x*(1-x))
	return 1/(1+exp(-x))

