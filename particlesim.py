from tkinter import *
import math

G = 0.0000000000667408
MASS_FACTOR = 10 ** 8


class Simulation(Canvas):
    
    def __init__(self, root, **kwargs):
        Canvas.__init__(self, master=root, **kwargs)

        self.particles = []

    def add(self, part, **kwargs):
        x1 = part.x - part.size/2
        y1 = part.y - part.size/2
        x2 = part.x + part.size/2
        y2 = part.y + part.size/2
        self.create_oval(x1, y1, x2, y2, **kwargs)
        self.particles += [part]

    def step(self, time):
        next_particles = [0 for x in self.particles]
        for index, shape in enumerate(self.particles):
            #print(shape)
            temp = Particle()
            temp.x = shape.x + shape.xVel * time
            temp.y = shape.y + shape.yVel * time
            temp.xVel = shape.xVel + shape.xAccel * time
            temp.yVel = shape.yVel + shape.yAccel * time
            temp.xAccel = 0
            temp.yAccel = 0
            for idx, s in enumerate(self.particles):
                if idx != index:
                    r = math.sqrt((shape.x - s.x) **2 + (shape.y - s.y) ** 2)
                    tmp = G * s.mass / r**3
                    temp.xAccel += tmp * (s.x - shape.x)
                    temp.yAccel += tmp * (s.y - shape.y)
            next_particles[index] = temp
        for index, shape in enumerate(self.particles):
            if not shape.stationary:
                self.move(index + 1, next_particles[index].x - shape.x, next_particles[index].y - shape.y)
                shape.get_attributes(next_particles[index])

    def make_lines(self):
        for shape in self.particles:
            self.create_line(shape.x, shape.y, shape.x+1, shape.y+1, fill=shape.color)
            

class Particle:
    def __init__(self, x=0, y=0, xVel=0, yVel=0, size=10, color=None, stationary=False):
        self.x = x
        self.y = y
        self.size = size
        self.mass = size * MASS_FACTOR
        self.color = color
        self.xVel = xVel
        self.yVel = yVel
        self.xForce = 0
        self.yForce = 0
        self.xAccel = 0
        self.yAccel = 0
        self.color = color
        self.stationary = stationary

    def __repr__(self):
        return 'Particle at ({0}, {1}), accel ({2}, {3}), speed ({4}, {5}) and forces ({6}, {7})'.format(self.x, self.y,
                                                                                                         self.xAccel, self.yAccel,
                                                                                                         self.xVel, self.yVel,
                                                                                                         self.xForce, self.yForce)
    def get_attributes(self, other):
        self.x = other.x
        self.y = other.y
        self.xVel = other.xVel
        self.yVel = other.yVel
        self.xForce = other.xForce
        self.yForce = other.yForce
        self.xAccel = other.xAccel
        self.yAccel = other.yAccel
    
    def dist(self, p2):
        return math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)