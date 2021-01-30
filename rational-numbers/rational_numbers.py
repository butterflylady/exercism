from __future__ import division
import math


class Rational:
    def __init__(self, numer, denom):
        gcd = math.gcd(numer, denom)
        if denom != 0 and numer != 0:
            self.numer = int((numer * denom) / abs(numer * denom) * abs(numer) / gcd)
            self.denom = int(abs(denom) / gcd)
        else:
            self.numer = int(numer / gcd)
            self.denom = int(denom / gcd)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power > 0:
            return Rational(self.numer ** power, self.denom ** power)
        if power == 0:
            return Rational(1, 1)
        if power < 0:
            return Rational(self.denom ** abs(power), self.numer ** abs(power))

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
