#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Number(object):

    def __init__(self, value):
        self.value = value
        self.is_pair = value % 2 == 0
        self.is_odd = value % 2 != 0

    @property
    def romam(self):
        roman_number = ''
        value = self.value
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_numbers = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 
               'V', 'IV', 'I']
        for i, number in enumerate(numbers):
            while value >= number:
                value -= number
                roman_number += roman_numbers[i]
        return roman_number

    @property
    def fibonacci(self):
        fibonacci = [1, 1]
        while 1:
            if self.value == fibonacci[-1]: return len(fibonacci)
            if fibonacci[-1] > self.value: return 'nao pertence'
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
            
    @property
    def loop_fatorial(self):
        fatorial = 1
        if self.value < 2: 
            return 1
        for i in range(2, self.value + 1):
            fatorial *= i
        return fatorial

    @property
    def recursive_fatorial(self):
        def calculate(num):
            return 1 if num < 2 else num * calculate(num - 1) 
        return  calculate(self.value)
        
    @property
    def functional_fatorial(self):
        return 1 if self.value < 2 else \
               reduce(lambda x, y: x * y, range(1, self.value + 1))
