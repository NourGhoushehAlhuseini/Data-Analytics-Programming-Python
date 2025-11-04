problem = "problem2"
student_name = "nour"
student_number = "t0326796"

from math import gcd

# PART A 
#  the class and implement basic data attributes and required dunder methods
class Fraction:
   

    def __init__(self, num, den):
        if den == 0:
            raise ValueError("Denominator cannot be zero.")
        if den < 0:
            num = -num
            den = -den
        self.num = num
        self.den = den
        self.reduce()  # simplify the fraction

    def __str__(self):
        # numerator / denomenator
        return f"{self.num}/{self.den}"

    def __add__(self, other): # adding two fractions using a common denominator
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other): # subtracting two fractions
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __float__(self):
        # converts to float for decimal representation
        return self.num / self.den

    # PART B 
    #  more  methods and custom methods like inverse
    def __mul__(self, other): #multiply numerators and denominators
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other): 
        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction.")
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        # check equality by comparing simplified numerators and denominators
        return self.num == other.num and self.den == other.den

    def __lt__(self, other):
        #less than comparison using cross multiplication
        return self.num * other.den < other.num * self.den

    def __le__(self, other): # less than comparison using cross multiplication
        return self.num * other.den <= other.num * self.den

    def __gt__(self, other): # greater than comparison
        return self.num * other.den > other.num * self.den

    def __ge__(self, other): # greater than or equal to comparison
        return self.num * other.den >= other.num * self.den

    def __pow__(self, power): # raise both numerator and denominator to the given power
        return Fraction(self.num ** power, self.den ** power)

    def reciprocal(self): 
        if self.num == 0:
            raise ZeroDivisionError("Cannot find reciprocal of zero.")
        return Fraction(self.den, self.num)

    #  PART C 
    # reduces the fraction to its simplest form using the GCD algorithm
    def reduce(self):
        common_divisor = gcd(self.num, self.den)
        self.num //= common_divisor
        self.den //= common_divisor



def get_fraction_input(prompt):
    while True:
        try:
            num = int(input(f"Enter the numerator for {prompt}: "))
            den = int(input(f"Enter the denominator for {prompt}: "))
            if den == 0:
                raise ValueError("Denominator cannot be zero. Please enter a valid denominator.")
            return Fraction(num, den)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
   
    # get 2 fractions from the user
    f1 = get_fraction_input("Fraction 1")
    f2 = get_fraction_input("Fraction 2")
    # show all operations and results 
    print("\nResults:")
    print(f"Fraction 1: {f1}")
    print(f"Fraction 2: {f2}")
    print(f"Decimal of {f1}: {float(f1)}")
    print(f"Decimal of {f2}: {float(f2)}")
    print(f"Addition: {f1} + {f2} = {f1 + f2}")
    print(f"Subtraction: {f1} - {f2} = {f1 - f2}")
    print(f"Multiplication: {f1} * {f2} = {f1 * f2}")
    print(f"Division: {f1} / {f2} = {f1 / f2}")
    print(f"Power: {f1} ** 2 = {f1 ** 2}")
    print(f"Reciprocal of {f1} = {f1.reciprocal()}")
    print(f"Reciprocal of {f2} = {f2.reciprocal()}")
    print(f"{f1} == {f2}: {f1 == f2}")
    print(f"{f1} > {f2}: {f1 > f2}")
    print(f"{f1} < {f2}: {f1 < f2}")
