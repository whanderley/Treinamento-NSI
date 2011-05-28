#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ComplexNumber(object):

    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def add(self, complex_number):
        return complex(self.real_part, self.imaginary_part) + \
          complex(complex_number.real_part, complex_number.imaginary_part)

    def subtract(self, complex_number):
        return complex(self.real_part, self.imaginary_part) - \
              complex(complex_number.real_part, complex_number.imaginary_part)

    def multiplication(self, complex_number):
        return complex(self.real_part, self.imaginary_part) * \
              complex(complex_number.real_part, complex_number.imaginary_part)

    def parse_to_string(self):
        return str(complex(self.real_part, self.imaginary_part))
