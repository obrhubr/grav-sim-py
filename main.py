import numpy as np
import pygame, math, sys
from lib.Planet import Planet
from lib.Simulate import simulate

sigma = int(sys.argv[1])
totaltime = int(sys.argv[2])

#enter values here
#(mass, acceleration-x-axis, acceleration-y-axis, position-x-axis, position-y-axis)
planet1 = Planet(1000000000000000000000000000000, 0, 0, 1, 2)
planet2 = Planet(1000000000000000000000000000, 0, -100000, 1000000000, 10)
planet3 = Planet(1000000000000000000000000000, 0, 100000, -1000000000, 10)
planetlist = [planet1, planet2, planet3]

simulate(sigma, totaltime, len(planetlist), planetlist)