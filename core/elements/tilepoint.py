#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .element import Element


class TilePoint(Element):

    def __init__(self):
        super(TilePoint, self).__init__()
        self.e = 0
        self.n = 0
        self.z = 0
        self.type = 'point'

    def add_e(self, e):
        if self.is_num(e):
            self.e = int(e)

    def add_n(self, n):
        if self.is_num(n):
            self.n = int(n)

    def add_z(self, z):
        if self.is_num(z):
            self.z = int(z)

    def add_coordinates(self, e, n, z=0):
        self.add_e(e)
        self.add_n(n)
        self.add_z(z)

    def is_valid(self):
        if self.is_num(self.e) is not True:
            return False

        if self.is_num(self.n) is not True:
            return False

        if self.is_num(self.z) is not True:
            return False

        return True

    def is_num(self, num):
        try:
            int(num)
            return True
        except ValueError:
            return False

    def get_str(self):
        s = Element.get_str(self)
        s += " e,n,z: "
        s += str(self.e) + ","
        s += str(self.n) + ","
        s += str(self.z)
        return s

    def get_dictionary(self):
        d = Element.get_dictionary(self)
        d['e'] = self.e
        d['n'] = self.n
        d['z'] = self.z
        return d

    def set_dictionary(self, d):
        Element.set_dictionary(self, d)
        self.add_coordinates(d['e'], d['n'], d['z'])

