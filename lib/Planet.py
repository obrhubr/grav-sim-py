import numpy as np
import pygame
import math

class Planet():
    def __init__(self, mass, accelerationx, accelerationy, positionx, positiony):
        self.mass = mass
        self.accelerationx = accelerationx
        self.accelerationy = accelerationy
        self.positionx = positionx
        self.positiony = positiony

    def distance(self, self2):
        distance = math.sqrt((math.pow(abs(self2.positionx - self.positionx), 2))+(math.pow(abs(self2.positiony - self.positiony),2)))
        return distance

    def move(self, self2, sigma):
        distance = self.distance(self2)
        cos = ((abs(self.positionx - self2.positionx))/distance)
        sin = ((abs(self.positiony - self2.positiony))/distance)
        force = ((0.0000000000667 * ((self2.mass)/(math.pow(distance, 2)))))

        if self.positionx < self2.positionx:
            self.accelerationx += ((abs(cos*force))/2*sigma)
        elif self.positionx > self2.positionx:
            self.accelerationx -= ((abs(cos*force))/2*sigma)
        if self.positiony < self2.positiony:
            self.accelerationy += ((abs(sin*force))/2*sigma)
        elif self.positiony > self2.positiony:
            self.accelerationy -= ((abs(sin*force))/2*sigma)