#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Television(object):

    def __init__(self, number_of_channels, maximum_volume):
        self.channel = 1
        self.volume = 0
        self.status = 'off'
        self.number_of_channels = number_of_channels
        self.maximum_volume = maximum_volume

    def press_power_button(self):
        self.status = 'on' if self.status == 'off' else 'off'
        return self.status

    def set_up_channel(self):
        if self.channel < self.number_of_channels:
            self.channel += 1
        return self.channel

    def set_down_channel(self):
        if self.channel > 1:
            self.channel -= 1
        return self.channel

    def set_up_volume(self):
        if self.volume < self.maximum_volume:
            self.volume += 1
        return self.volume

    def set_down_volume(self):
        if self.volume > 0:
            self.volume -= 1
        return self.volume
