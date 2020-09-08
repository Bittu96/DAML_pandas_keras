import math
from math import *
import numpy
from numpy import *
import time
import pygame
from pygame import *
import sys, pygame, math, os, random
from pygame.locals import *

pygame.init()
size=width,height=800,500
screen=pygame.display.set_mode(size)
pygame.display.set_caption("inverted_pendulum_balancing")
acc = 0
training_data = [[],[]]
t = 0
while t<20:
  key=pygame.key.get_pressed()
  if key[pygame.K_UP]:   
    acc+=0.8
    training_data[0].append(1)
  elif key[pygame.K_DOWN]: 
    acc-=0.8
    training_data[0].append(-1)
  else:
    acc=0
    training_data[0].append(0)
  t += 0.01
  
  bgcolour=(0,0,0) 
  screen.fill(bgcolour)
  for event in pygame.event.get(): 
    if event.type==pygame.QUIT:sys.exit()
  pygame.display.flip();pygame.time.delay(10)
  pygame.display.update()