#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Rectangle2(object):

    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.center = [base/2, height/2]

    def redefine_vertices(self):
        self.vertice1 = Point(self.center[0] - self.base/2,
                         self.center[1] - self.height/2)
        self.vertice2 = Point(self.center[0] - self.base/2,
                        self.center[1] + self.height/2)
        self.vertice3 = Point(self.center[0] + self.base/2,
                        self.center[1] + self.height/2)
        self.vertice4 = Point(self.center[0] + self.base/2,
                        self.center[1] - self.height/2)

    def redefine_center(self, x, y):
        self.center = [x, y]
        self.redefine_vertices()
        return self.center

    @property
    def area(self):
        return self.base * self.height

    @property
    def perimeter(self):
        return (self.base + self.height) * 2

    def is_square(self):
        return self.base == self.height


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
