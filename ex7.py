#!/usr/bin/env python
# -*- coding: utf-8 -*-


class GasolinePump(object):

    def __init__(self, capacity, price_per_liter):
        self.capacity = capacity
        self.volume = capacity
        self.price_per_liter = price_per_liter

    def fill(self):
        self.volume = self.capacity
        return self.volume

    def supply_by_value(self, value):
        if round(value / self.price_per_liter) > self.volume:
            return 'volume unavailable'
        self.volume -= round(value / float(self.price_per_liter))
        return round(value / float(self.price_per_liter))

    def supply_by_number_of_liters(self, volume):
        if volume > self.volume:
            return 'volume unavailable'
        self.volume -= volume
        return volume * self.price_per_liter
