# Să se scrie o clasă Fractie(numarator, numitor) care sa implementeze următoarele metode:
class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator

    def __str__(self):
        return str(self.top) + "/" + str(self.bottom)

    def __add__(self, other):
        newtop = self.top * other.bottom + other.top * self.bottom
        newbottom = self.bottom * other.bottom
        return Fraction(newtop, newbottom)

    def __sub__(self, other):
        newtop = self.top * other.bottom - other.top * self.bottom
        newbottom = self.bottom * other.bottom
        return Fraction(newtop, newbottom)

    def inverse(self):
        return Fraction(self.bottom,self.top)
    # sau
    def __invert__(self):
        return Fraction(self.bottom,self.top)

t = Fraction(15,21)
print(f't={t}')
b = Fraction(17,5)
print(f'b={b}')
print(f't+b = {t+b}')
print(f't-b = {t-b}')
print(f'Inverse of t ={t.inverse()}')
print(f'Inverse of b = {b.inverse()}')
#sau
print(f'{t.__invert__()}')
print(f'{b.__invert__()}')
#sau
print(Fraction.inverse(t))
print(Fraction.inverse(b))


