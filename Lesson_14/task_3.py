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

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Cannot add a Fraction with a non-Fraction type")
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator).reduce()

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Cannot subtract a non-Fraction type from a Fraction")
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator).reduce()

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Cannot multiply a Fraction with a non-Fraction type")
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator).reduce()

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Cannot divide a Fraction by a non-Fraction type")
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator).reduce()

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Cannot compare a Fraction with a non-Fraction type")
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Cannot compare a Fraction with a non-Fraction type")
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Cannot compare a Fraction with a non-Fraction type")
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Cannot compare a Fraction with a non-Fraction type")
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __str__(self):
        whole_part = self.numerator // self.denominator
        numerator = self.numerator % self.denominator
        if whole_part == 0:
            return f"{numerator}/{self.denominator}"
        elif numerator == 0:
            return str(whole_part)
        else:
            return f"{whole_part} {numerator}/{self.denominator}"


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)

    z = x + y
    print(z)  # print "3/4"

    z = x - y
    print(z)  # print "1/4"

    z = x * y
    print(z)  # print "1/8"

    z = x / y
    print(z)  # print "2/1"

    print(x + y == Fraction(3, 4))  # must be True
    print(x == y) # must be False
    print(x > y)  # must be True
    print(x < y)  # must be False
    print(x >= y)  # must be True
    print(x <= y)  # must be False


