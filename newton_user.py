from newton import runPG
import math


f = lambda x : math.exp(-x) + x - 2
f1 = lambda x : -math.exp(-x) + 1
stop = .0001
x0 = -3
scale = 20

runPG(f, f1, x0, scale, stop)
