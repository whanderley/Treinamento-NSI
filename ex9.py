#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Carnivorous(object):

    def  __init__(self):
        self.stomach = []

    def eat(self, food):
        self.stomach.append(food)
        return self.stomach

    def digest(self):
        return self.stomach.pop(0)
