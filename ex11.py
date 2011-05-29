#!/usr/bin/env python
# -*- coding: utf-8 -*-


class RacionalNumber(object):

    def __init__(self, numerator, denominador):
        self.reduced_form(numerator, denominador)

    def __eq__(self, racional_number):
        return self.numerator == racional_number.numerator and \
        self.denominador == racional_number.denominador

    def __add__(self, racional_number):
        numerator = self.numerator * racional_number.denominador + \
        racional_number.numerator * self.denominador
        denominador = self.denominador * racional_number.denominador
        return RacionalNumber(numerator, denominador)

    def __sub__(self, racional_number):
        numerator = self.numerator * racional_number.denominador - \
        racional_number.numerator * self.denominador
        denominador = self.denominador * racional_number.denominador
        return RacionalNumber(numerator, denominador)

    def __mul__(self, racional_number):
        numerator = self.numerator * racional_number.numerator
        denominador = self.denominador * racional_number.denominador
        return RacionalNumber(numerator, denominador)

    def __div__(self, racional_number):
        numerator = self.numerator * racional_number.denominador
        denominador = self.denominador * racional_number.numerator
        return RacionalNumber(numerator, denominador)

    @property
    def string(self):
        return '%s/%s' %(self.numerator, self.denominador)

    def float_string(self, lenght):
        number = self.numerator / float(self.denominador)
        return str(number)[:lenght + 1]

    def reduced_form(self, numerator, denominador):
        divisor = None
        i = 2
        while i <= numerator and i <= denominador:
            if denominador % i == 0 and numerator % i == 0:
                divisor = i
            i += 1
        if divisor:
            self.numerator = (numerator / divisor)
            self.denominador = (denominador / divisor)
        else:
            self.numerator = numerator
            self.denominador = denominador
