from newton import runPG

import pygame
from time import sleep
import numpy as np
import math
from pygame.locals import *
import random
import itertools


f = lambda x : x**2 * math.exp(x) * 3 - 1
f1 = lambda x : 6* x * math.exp(x) + 3 * x**2 * math.exp(x)
stop = .001
x0 = -6
scale = 30

runPG(f, f1, x0, scale, stop)
