from Grid import *
from Mesh3D import *
from Transform import *
from Button import Button
from DisplayNormals import *

class Object:
    def __init__(self, obj_name):
        self.name = obj_name
        self.components = []
        self.scene_angle = 0

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
                self.scene_angle += 0.5
                glRotate(self.scene_angle, 0, 1, 0)

            elif isinstance(component, Mesh3D):
                glColor3f(1, 1, 1)
                component.draw()

            elif isinstance(component, Grid):
                component.draw()

            elif isinstance(component, DisplayNormals):
                component.draw()

            elif isinstance(component, Button):
                component.draw(events)

        glPopMatrix()

    def get_component(self, class_type):
        for c in self.components:
            if type(c) is class_type:
                return c
        return None