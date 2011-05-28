#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-*- coding: utf-8 -*-


class Square(object):

    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** 2
