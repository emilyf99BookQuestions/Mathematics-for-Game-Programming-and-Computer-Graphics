from Mesh3D import *
from Transform import *
from Button import Button

class Object:
    def __init__(self, obj_name):
        self.name = obj_name
        self.components = []

    def add_component(self, component):
        if isinstance(component, Transform):
            self.components.insert(0, component)

        self.components.append(component)

    def update(self, events = None):
        glPushMatrix()
        for component in self.components:
            if isinstance(component, Transform):
                pos = component.get_position()
                glTranslatef(pos.x, pos.y, pos.z)

            if isinstance(component, Mesh3D):
                component.draw()

            if isinstance(component, Button):
                component.draw(events)

        glPopMatrix()

    def get_component(self, class_type):
        for c in self.components:
            if type(c) is class_type:
                return c
        return None