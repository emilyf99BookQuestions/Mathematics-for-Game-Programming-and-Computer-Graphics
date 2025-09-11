import pygame
from OpenGL import *
from OpenGL.GL import *
from MathOGL import *

class DisplayNormals:

    def __init__(self, vertices, triangles):
        self.vertices = vertices
        self.triangles = triangles
        self.normals = []

        for t in range(0, len(self.triangles), 3):
            i1 = self.triangles[t]
            i2 = self.triangles[t + 1]
            i3 = self.triangles[t + 2]

            vertex1 = pygame.Vector3(self.vertices[i1])
            vertex2 = pygame.Vector3(self.vertices[i2])
            vertex3 = pygame.Vector3(self.vertices[i3])

            # Two edge vectors
            p = vertex2 - vertex1
            q = vertex3 - vertex1

            # normal via cross product
            norm = cross_product(p ,q)
            norm = norm.normalize()

            centroid = (vertex1 + vertex2+ vertex3) / 3

            self.normals.append((centroid, centroid + norm))

    def draw(self):
        glColor3fv((0, 1, 0))
        glBegin(GL_LINES)

        for i in range(0, len(self.normals)):
            start_point = self.normals[i][0]
            end_point = self.normals[i][1]
            glVertex3fv((start_point[0], start_point[1], start_point[2]))
            glVertex3fv((end_point[0], end_point[1], end_point[2]))
        glEnd()

        pass
