#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Rectangle(object):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    @property
    def area(self):
        return self.base * self.height

    @property
    def perimeter(self):
        return (self.base * 2) + (self.height * 2)
