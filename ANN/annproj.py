import math
from math import *

import numpy as np
from numpy import *

import time
import pygame
from pygame import *

import sys, pygame, math, os, random
from pygame.locals import *

#random.seed(1)

nodes_in_input_layer = 4
nodes_in_hiddenlayer = 6
nodes_in_outputlayer = 2

num_pop_set,weights = 10,nodes_in_hiddenlayer

pop_size = (num_pop_set,weights)

population = 0.001*(np.random.randint(-1000, 1000, size=(10, nodes_in_hiddenlayer, nodes_in_input_layer+nodes_in_outputlayer)))
#print population[0]

pygame.init()
size=width,height=800,600

screen=pygame.display.set_mode(size)
pygame.display.set_caption("Self Learning Robotic Arm")

font = pygame.font.SysFont("comicsansms", 30)
text = font.render("2 link arm \n learning...", True, (255, 255, 255))

(bx,by) = (400,300)

l1 = 100
l2 = 100

m1 = 10
m2 = 10

g = 9.81

tx,ty = 0,200
#target_state = [bx+tx,by-ty]
target_state = [bx+tx,by-ty,0,0]
state = [0,0,0,0]

def sigm(x, deriv=False):
  if(deriv==True):
    return (x*(1-x))
  return 1/(1+ exp(-x))

def ann(x,w):
  l = 1
  wt0 = w[0:4]
  wt1 = w[4:6].T

  #print "x:",x,"\nwt0:",wt0,"\nwt1:",wt1
  l0 = mat(x)
  l1 = sigm(dot(l0, wt0))
  l2 = sigm(dot(l1, wt1))
  #print l2

  return l2


def fitness(st):
  fitness = 0

  for i in xrange(len(st)):
    fitness += (st[i] - target_state[i])**2
  
  fitness = sqrt(fitness)/400
  return fitness


def test(pop):
  global state
  tor = 0.1*(ravel(ann(state,pop)) - 0.5)
  torque1,torque2=tor[0],tor[1] 
  #print tor
  theta1 = 0
  theta2 = 0
  omega1 = omega2 = 0
  loss = 0.8
  sim_time = 0

  while sim_time < 2 :
    tor = (ravel(ann(state,pop)) - 0.5)*2
    #print tor
    torque1,torque2=0.2*tor[0],0.1*tor[1] 
    alpha1 = torque1 + ( (-g*(2*m1 + m2)*sin(theta1)) - (m2*g*sin(theta1 - 2*theta2)) - (2*sin(theta1-theta2)*m2*(l2*omega2**2 + l1*cos(theta1-theta2)*omega1**2 ))  )/( l1*(2*m1 + m2 - m2*cos(2*theta1 - 2*theta2)) )
    alpha2 = torque2 + 2*sin(theta1-theta2) * ((l1*(m1+m2)*omega1**2) + (g*(m1+m2)*cos(theta1)) + (m2*l2*cos(theta1-theta2)*omega2**2) )/( l2*(2*m1 + m2 - m2*cos(2*theta1 - 2*theta2)) )

    #print alpha1,alpha2

    x1 = bx + l1*sin(theta1)
    y1 = by + l1*cos(theta1)

    x2 = x1 + l2*sin(theta2)
    y2 = y1 + l2*cos(theta2)
    
    omega1 += (alpha1 - omega1*loss)
    omega2 += (alpha2 - omega2*loss)

    theta1 += (omega1)
    theta2 += (omega2)

    state = [theta1,theta2,omega1,omega2]

    bgcolour=(0,0,0) 
    screen.fill(bgcolour)
    
    for event in pygame.event.get(): 
      if event.type==pygame.QUIT:sys.exit()

    pygame.draw.line(screen, (255,255,255), (400,600), (400,0), 1)
    pygame.draw.line(screen, (255,255,255), (0,300), (800,300), 1)

    pygame.draw.line(screen, (255,0,0), (bx,by), (x1,y1), 5)
    pygame.draw.line(screen, (255,0,0), (x1,y1), (x2,y2), 5)
    
    pygame.draw.circle(screen, (255,100,255), (bx,by), m1)
    pygame.draw.circle(screen, (255,100,255), (int(nan_to_num(x1)),int(nan_to_num(y1))), m2)

    screen.blit(text,(150 - text.get_width() // 2, 100 - text.get_height() // 2))
    
    pygame.display.flip();pygame.time.delay(0)

    pygame.display.update()

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('ANN+GEN', False, (0, 0, 0))
    screen.blit(textsurface,(100,100))
    #print 'fitness:',fitness([x2,y2])
    #print [x2,y2]
    sim_time+=0.01

  #print 'fitness:',fitness([x2,y2])
  return fitness([x2,y2])



def best_of_population(arr):
  m1 = fitness_arr.index(min(fitness_arr))

  temp = fitness_arr
  temp.remove(min(fitness_arr))

  m2 = fitness_arr.index(min(temp))
  #print m1,m2
  return (population[m1],population[m2])


def breeding(bred):
  new = []

  child1 = join(bred[0][0:3],bred[1][3:6])
  child2 = join(bred[1][0:3],bred[0][3:6])
  
  child3 = join(bred[0][3:6],bred[1][0:3])
  child4 = join(bred[1][3:6],bred[0][0:3])
  
  child5 = join(bred[0][0:4],bred[1][4:6])
  child6 = join(bred[1][0:4],bred[0][4:6])

  child7 = join(bred[0][4:6],bred[1][0:4])
  child8 = join(bred[1][4:6],bred[0][0:4])

  newrand = 0.001*(np.random.randint(-1000, 1000, size=(4, 6, 6)))
  new.append(bred[0])
  new.append(bred[1])
  new.append(child1)
  new.append(child2)
  new.append(child3)
  new.append(child4)
  new.append(child5)
  new.append(child6)
  new.append(newrand[0])
  new.append(newrand[1])
  #new.append(newrand[2])
  #new.append(newrand[3])
  #print new
  return new

def join(p1,p2):
  temp=[]
  for i in xrange(len(p1)):
    temp.append(list(ravel(p1[i])))
  for i in xrange(len(p2)):
    temp.append(list(ravel(p2[i])))
  return mat(temp)

def next_gen_population(fam):
  num_pop_set,weights = 2,6

  pop_size = (num_pop_set,weights)

  new_population = 0.001*(np.random.randint(-1000, 1000, size=(2, 6, 6)))

  fin = fam#concatenate((array(fam),array(new_population)))
  return fin

'''
def trainANN(tordat):
  l = 1
  x = tordat
  y = target_state

  for j in xrange(10000):
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
'''
gen = 1

test(population[0])

while 1:
  fitness_arr = []

  for i in xrange(10):
    fitness_arr.append(test(population[i]))
  best =  best_of_population(fitness_arr)
  #print "GENERATION ",gen,'->','bestfit:',min(fitness_arr),'\t','avg_fit:',mean(fitness_arr)
  print min(fitness_arr),mean(fitness_arr)
  newfam = breeding(best)
  ngp = next_gen_population(newfam)
  #print 'best: ',best,'\n','newfam: ',newfam,'\n','ngp: ',ngp
  population = ngp
  gen+=1
