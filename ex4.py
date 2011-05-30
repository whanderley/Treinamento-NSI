#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person(object):

    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height

    def get_old(self):
        self.age += 1
        if self.age <= 21:
            self.height += 1.5
        return self.age

    def fatten(self, kg):
        self.weight += kg
        return self.weight

    def weight_loss(self, kg):
        self.weight -= kg
        return self.weight
