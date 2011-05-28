#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CurrentAccount(object):

    def __init__(self, holder_name, account_number):
        self.holder_name = holder_name
        self.account_number = account_number
        self.leftover = 0

    def deposit(self, value):
        self.leftover += value
        return self.leftover

    def retire(self, value):
        if self.leftover < value:
            return "not enough money"
        self.leftover -= value
        return self.leftover
