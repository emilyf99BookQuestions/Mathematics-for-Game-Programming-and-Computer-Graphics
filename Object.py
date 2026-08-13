from Grid import *
from Mesh3D import *
from Transform import *
from Button import Button
from DisplayNormals import *
from Camera import *

class Object:
    def __init__(self, obj_name):
        self.name = obj_name
        self.components = []
        self.scene_angle = 45

    def add_component(self, component):
        if isinstance(component, Transform):
            self.components.insert(0, self.components)
        self.components.append(component)

    def get_component(self, class_type):
        for c in self.components:
            if type(c) is class_type:
                return c
        return None


    def update(self, camera: Camera, events = None):
        glPushMatrix()
        for component in self.components:
            if isinstance(component, Transform):
               glLoadMatrixf(component.get_MVM() * camera.get_VM())

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
