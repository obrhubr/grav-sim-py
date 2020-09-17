import numpy as np
import pygame
import math

class Planet():
    def __init__(self, mass, accelerationx, accelerationy, positionx, positiony):
        self.mass, self.accelerationx, self.accelerationy, self.positionx, self.positiony = mass, accelerationx, accelerationy, positionx, positiony

    def distance(self, self2):
        return math.sqrt((math.pow(abs(self2.positionx - self.positionx), 2))+(math.pow(abs(self2.positiony - self.positiony),2)))

    def move(self, self2, sigma):
        distance = self.distance(self2)
        force = ((0.0000000000667 * ((self2.mass)/(math.pow(distance, 2)))))
        self.accelerationx -= ((((self.positionx - self2.positionx)/distance)*force)/2*sigma)
        self.accelerationy -= ((((self.positiony - self2.positiony)/distance)*force)/2*sigma)