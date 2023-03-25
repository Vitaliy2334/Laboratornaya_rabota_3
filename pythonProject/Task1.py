class Fraction(object):
    def __init__(self, num, den):
        self.__num = num
        self.__den = den
        self.reduce()

    def __str__(self):
        return "%d/%d" % (self.__num, self.__den)

    def reduce(self):
        g = Fraction.gcd(self.__num, self.__den)
        self.__num //= g
        self.__den //= g

    def __neg__(self):  # возвращает новый объект с противоположенным числителем
        return Fraction(-self.__num, self.__den)

    def __invert__(self):  # возвращает новый объект с поменяными местами числителем и знаменателем
        return Fraction(self.__den, self.__num)

    def __pow__(self, power, modulo=None):  # возведение в степень
        return Fraction(self.__num**power, self.__den**power)

    def __float__(self):  # вовращает вещественсное значение дроби
        return float(self.__num) / self.__den

    def __int__(self):  # возвращает целое значение дроби
        return self.__num // self.__den

    @staticmethod
    def gcd(n, m):
        if m == 0:
            return n
        else:
            return Fraction.gcd(m, n % m)
