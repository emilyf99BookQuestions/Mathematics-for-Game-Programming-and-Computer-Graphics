import pygame
import math
import numpy as np
from pygame.fastevent import post


class Camera:
    def __init__(self):
        self.VM = np.identity(4)

    def get_VM(self):
        return self.VM

    def get_position(self):
        position = pygame.math.Vector3(self.VM[0, 3], self.VM[1, 3], self.VM[2, 3])
        return position

    def update_position(self, position: pygame.Vector3):
        self.VM = self.VM @ np.matrix(
            [[1, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0],
             [position.x, position.y, position.z, 1]]
        )

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.update_position(self.get_position() + pygame.Vector3(0, 0, 0.01))
        if key[pygame.K_s]:
            self.update_position(self.get_position() + pygame.Vector3(0, 0, -0.01))