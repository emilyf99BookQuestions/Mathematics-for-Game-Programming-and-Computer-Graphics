import pygame

from Object import *
from Cube import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from Settings import *
from Grid import *

# Window Set Up
pygame.init()
screen_width = math.fabs(window_dimensions[1] - window_dimensions[0])
screen_height = math.fabs(window_dimensions[3] - window_dimensions[2])

pygame.display.set_caption(('OpenGL in Python'))
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)

done = False
objects_3d = []
objects_2d = []

# Object Set Up
cube = Object("Cube")
cube.add_component(Transform((0, 0, -5)))
cube.add_component(Cube(GL_POLYGON, "brushwalker218.tif"))
objects_3d.append(cube)


# Grid Set Up
grid = Object("Grid")
grid.add_component(Transform((0, 0, -5)))
grid.add_component(Grid(0.5, 8, (0, 0, 255)))

#objects_3d.append(grid)

clock = pygame.time.Clock()
fps = 30

def set_2d():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(gui_dimensions[0], gui_dimensions[1], gui_dimensions[3], gui_dimensions[2])

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())

def set_3d():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)

trans: Transform = cube.get_component(Transform)

while not done:
    events = pygame.event.get()

    glPushMatrix()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    set_3d()
    for o in objects_3d:
        o.update(events)

    set_2d()
    for o in objects_2d:
        o.update(events)

    glPopMatrix()
    pygame.display.flip()
    clock.tick(fps)

    for event in events:
        if event.type == pygame.QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                trans.move(pygame.Vector3(1, 1, -1))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        trans.update_rotation_angle(5)
    if keys[pygame.K_RIGHT]:
        trans.update_rotation_angle(-5)
    if keys[pygame.K_UP]:
        current = trans.get_scale()
        trans.set_scale(current * 1.1)
    if keys[pygame.K_DOWN]:
        current = trans.get_scale()
        trans.set_scale(current * 0.9)

