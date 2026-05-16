import pygame

class Transform:
    def __init__(self, position = pygame.Vector3(0,0,0), scale = pygame.Vector3(1,1,1)):
        self.position = pygame.Vector3(position)
        self.scale = pygame.Vector3(scale)
        self.rotation_angle = 0
        self.rotation_axis = pygame.Vector3(0, 1, 0)

    def get_rotation_angle(self):
        return self.rotation_angle

    # No setter for this

    def get_rotation_axis(self):
        return self.rotation_axis

    def set_rotation_axis(self, amount: pygame.Vector3):
        self.rotation_axis = amount

    def update_rotation_angle(self, amount):
        self.rotation_angle += amount

    def get_scale(self):
        return self.scale

    def set_scale(self, amount: pygame.Vector3):
        self.scale = amount

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = pygame.math.Vector3(position)

    def move_x(self, amount):
        self.position = pygame.math.Vector3(self.position.x + amount, self.position.y, self.position.z)

    def move_y(self,amount):
        self.position = pygame.math.Vector3(self.position.x, self.position.y + amount, self.position.z)

    def move(self, amount: pygame.math.Vector3):
        self.position = pygame.math.Vector3 (
            self.position.x + amount.x,
            self.position.y + amount.y,
            self.position.z + amount.z)