from Mesh3D import *
from Transform import *

class Object:
    def __init__(self, obj_name):
        self.name = obj_name
        self.components = []

    def add_component(self, component):
        if isinstance(component, Transform):
            self.components.insert(0, self.components)

        self.components.append(component)

    def update(self):
        glPushMatrix()
        for component in self.components:
            if isinstance(component, Transform):
                pos = component.get_position()
                glTranslatef(pos.x, pos.y, pos.z)
            if isinstance(component, Mesh3D):
                component.draw()
        glPopMatrix()