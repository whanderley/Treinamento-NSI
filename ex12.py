#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Number(object):

    def __init__(self, value):
        self.value = value
        self.is_pair = value % 2 == 0
        self.is_odd = value % 2 != 0

    @property
    def romam(self):
        value = self.value
        romans = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 
                    50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        roman_number = ''
        for number in romans:
            while value >= number:
                value -= number
                roman_number += romans[number]
        return roman_number

    @property
    def fibonacci(self):
        fibonacci = [1, 1]
        while 1:
            if self.value == fibonacci[-1]: return len(fibonacci)
            if fibonacci[-1] > self.value: return 'não pertence'
            fibonacci.append(fibonacci[-1] + fibonacci[-2])

    @property
    def loop_fatorial(self):
        fatorial = 0
        if self.value < 2: return 1
        for i in range(2, self.value + 1):
            fatorial *= i
        return fatorial

    @property
    def recursive_fatorial(self):
        if self.value < 2: return 1
        return self.value * Number(self.value -1).recursive_fatorial()

    @property
    def functional_fatorial(self):
        return 1 if self.value < 2 else \
        reduce(lambda x, y: x * y, range(1, self.value + 1))
