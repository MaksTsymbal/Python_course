# Create a Fraction class that will represent all the basic arithmetic logic for fractions (+, -, /, *)
# with proper error checking and handling. You need to add magic methods for mathematical operations
# and comparison operations between objects of the Fraction class

class Fraction:

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator

    def reduce(self):
        gcd = self._gcd(self.numerator, self.denominator)
        return Fraction(self.numerator // gcd, self.denominator // gcd)

    def _gcd(self, a, b):
        if b == 0:
            return a
        return self._gcd(b, a % b)

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator).reduce()

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator).reduce()

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator).reduce()

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator).reduce()

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return self.numerator == other.numerator and self.denominator == other.denominator


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)

    z = x + y
    print(z)  # print "6/8"

    z = x - y
    print(z)  # print "2/8"

    z = x * y
    print(z)  # print "1/8"

    z = x / y
    print(z)  # print "4/2"

    print(x + y == Fraction(3, 4))  # must be True
