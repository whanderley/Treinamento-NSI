#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ComplexNumber(object):

    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part
    
    def __eq__(self, complex_number):
        return self.real_part == complex_number.real_part and \
          self.imaginary_part == complex_number.imaginary_part

    def __add__(self, complex_number):
        real_part = self.real_part + complex_number.real_part
        imaginary_part = self.imaginary_part + complex_number.imaginary_part
        return ComplexNumber(real_part, imaginary_part)

    def __sub__(self, complex_number):
        real_part = self.real_part - complex_number.real_part
        imaginary_part = self.imaginary_part - complex_number.imaginary_part
        return ComplexNumber(real_part, imaginary_part)

    def __mul__(self, complex_number):
        real_part = self.real_part * complex_number.real_part - \
         self.imaginary_part * complex_number.imaginary_part
        imaginary_part = self.imaginary_part * complex_number.real_part + \
         self.real_part * complex_number.imaginary_part
        return ComplexNumber(real_part, imaginary_part)

    def __div__(self, complex_number):
        real_part = ((self.real_part * complex_number.real_part + 
         self.imaginary_part * complex_number.imaginary_part) / float(
          complex_number.real_part ** 2 + complex_number.imaginary_part ** 2))
        imaginary_part = ((self.imaginary_part * complex_number.real_part -
         self.real_part * complex_number.imaginary_part) / float(
           complex_number.real_part ** 2 + complex_number.imaginary_part ** 2))
        return ComplexNumber(round(real_part, 2), round(imaginary_part, 1))

    def parse_to_string(self):
        if self.imaginary_part > 0:
            return '%s + %si' % (self.real_part, self.imaginary_part)
        return '%s - %si' % (self.real_part, abs(self.imaginary_part))
