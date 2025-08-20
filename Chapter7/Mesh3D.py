import pygame.image
from OpenGL.GL import *


class Mesh3D:
    def __init__(self, filename):
        self.texture = pygame.image.load(filename)
        self.texID = 0

    def draw(self):
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glBindTexture(GL_TEXTURE_2D, self.texID)

        glBegin(GL_TRIANGLES)
        for i in range(len(self.triangles)):
            vertex_index = self.triangles[i]
            glTexCoord2fv(self.uvs[vertex_index])
            glVertex3fv(self.vertices[vertex_index])
        glEnd()
        glDisable(GL_TEXTURE_2D)

    def init_texture(self):
        self.texID = glGenTextures(1)
        textureData = pygame.image.tostring(self.texture, "RGB", 1)

        width = self.texture.get_width()
        height = self.texture.get_height()
        glBindTexture(GL_TEXTURE_2D, self.texID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0 , GL_RGB, GL_UNSIGNED_BYTE, textureData)
