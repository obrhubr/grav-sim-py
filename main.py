import numpy as np
import pygame, math, sys, argparse
from lib.Planet import Planet
from lib.Simulate import simulate

parser = argparse.ArgumentParser(description='Simulate Gravity. Use arguments: -s sigma in seconds, -t totaltime in seconds, -f export filename')
parser.add_argument('-s', '--sigma', type=float, metavar='', required=False, help='\033[93mThe time step for the simulation\033[0m')
parser.add_argument('-t', '--totaltime', type=int, metavar='', required=False, help='\033[93mThe total time for the simulation\033[0m')
parser.add_argument('-f', '--file', type=str, metavar='', required=False, help='\033[93mThe filename for the .npz export\033[0m')
args = parser.parse_args()

sigma = 1 if args.file is None else float(args.sigma)
totaltime = 50000 if args.file is None else int(args.totaltime)
filename = "Gravdata" if args.file is None else str(args.file)

#(mass, acceleration-x-axis, acceleration-y-axis, position-x-axis, position-y-axis)
planet1 = Planet(1000000000000000000000000000000, 0, 0, 1, 2)
planet2 = Planet(1000000000000000000000000000, 0, -100000, 1000000000, 10)
planet3 = Planet(1000000000000000000000000000, 0, 100000, -1000000000, 10)
planetlist = [planet1, planet2, planet3]

simulate(sigma, totaltime, len(planetlist), planetlist, filename)