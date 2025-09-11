from OpenGL.GL import *

class Grid():
    def __init__(self, interval, halfsize, colour):
        self.interval = interval
        self.halfsize = halfsize
        self.colour = colour

    def draw(self):
        glColor3fv(self.colour)
        glBegin(GL_LINES)

        for x in range(-self.halfsize, self.halfsize):
            for y in range(-self.halfsize, self.halfsize):
                # Vertical line at x
                glVertex3fv((x * self.interval, -self.halfsize * self.interval, 0))
                glVertex3fv((x * self.interval,  self.halfsize * self.interval, 0))

                # Horizontal line at y
                glVertex3fv((-self.halfsize * self.interval, y * self.interval, 0))
                glVertex3fv(( self.halfsize * self.interval, y * self.interval, 0))

        glEnd()
