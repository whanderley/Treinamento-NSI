#!/usr/bin/env python
# -*- coding: utf-8 -*-


class RacionalNumber(object):

    def __init__(self, numerator, denominator):
        self.reduced_form(numerator, denominator)

    def __eq__(self, racional_number):
        return self.numerator == racional_number.numerator and \
        self.denominator == racional_number.denominator

    def __add__(self, racional_number):
        numerator = self.numerator * racional_number.denominator + \
        racional_number.numerator * self.denominator
        denominator = self.denominator * racional_number.denominator
        return RacionalNumber(numerator, denominator)

    def __sub__(self, racional_number):
        numerator = self.numerator * racional_number.denominator - \
        racional_number.numerator * self.denominator
        denominator = self.denominator * racional_number.denominator
        return RacionalNumber(numerator, denominator)

    def __mul__(self, racional_number):
        numerator = self.numerator * racional_number.numerator
        denominator = self.denominator * racional_number.denominator
        return RacionalNumber(numerator, denominator)

    def __div__(self, racional_number):
        numerator = self.numerator * racional_number.denominator
        denominator = self.denominator * racional_number.numerator
        return RacionalNumber(numerator, denominator)

    @property
    def string(self):
        return '%s/%s' % (self.numerator, self.denominator)

    def float_string(self, lenght):
        number = self.numerator / float(self.denominator)
        return str(number)[:lenght + 1]

    def reduced_form(self, numerator, denominator):
        divisor = None
        i = 2
        while i <= numerator and i <= denominator:
            if denominator % i == 0 and numerator % i == 0:
                divisor = i
            i += 1
        if divisor:
            self.numerator = (numerator / divisor)
            self.denominator = (denominator / divisor)
        else:
            self.numerator = numerator
            self.denominator = denominator
