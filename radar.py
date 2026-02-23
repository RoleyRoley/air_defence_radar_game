# Handles radar behavior like target detection.

import pygame
import math
import random

pygame.display.set_caption("Radar Sweep Animation")



class Radar:
    def __init__(self, radius, sweep_speed):
        self.radius = radius
        self.sweep_speed = sweep_speed
        self.angle = 0