#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person(object):

    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height

    def get_old(self, past_years):
        if self.age + past_years < 21:
            self.height += past_years * 1.5
        else:
            self.height += (21 - self.age) * 1.5
        self.age += past_years
        return self.age

    def fatten(self, kg):
        self.weight += kg
        return self.weight

    def weight_loss(self, kg):
        self.weight -= kg
        return self.weight
