from math import gcd

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

# Примеры использования

frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)

print(f"{frac1} + {frac2} = {frac1 + frac2}")
print(f"{frac1} - {frac2} = {frac1 - frac2}")
print(f"{frac1} * {frac2} = {frac1 * frac2}")
print(f"{frac1} / {frac2} = {frac1 / frac2}")

print(f"{frac1} == {frac2} : {frac1 == frac2}")
print(f"{frac1} < {frac2} : {frac1 < frac2}")
print(f"{frac1} <= {frac2} : {frac1 <= frac2}")
print(f"{frac1} > {frac2} : {frac1 > frac2}")
print(f"{frac1} >= {frac2} : {frac1 >= frac2}")
