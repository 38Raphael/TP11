class Rational:
    def __init__(self, num, deno):
        self.__denom = deno
        self.__nume = num

    def __add__(self, other):
        if isinstance(other, Rational) is True:
            return Rational(self.__nume * other.__denom + other.__nume * self.__denom, self.__denom * other.__denom)

    def __sub__(self, other):
        if isinstance(other, Rational) is True:
            return Rational(self.__nume * other.__denom - other.__nume * self.__denom, self.__denom * other.__denom)

    def __rsub__(self, other):
        if isinstance(other, Rational) is True:
            return Rational(other.__nume * self.__denom - self.__nume * other.__denom, self.__denom * other.__denom)

    def __radd__(self, other):
        if isinstance(other, Rational) is True:
            return Rational(other.__nume * self.__denom + self.__nume * other.__denom, other.__denom * self.__denom)

    def __mul__(self, other):
        if isinstance(other, Rational) is True:
            return Rational(self.__nume * other.__nume, self.__denom * other.__denom)

    def __truediv__(self, other):
        if isinstance(other, Rational) is True:
            return Rational(self.__nume * other.__denom, self.__denom * other.__nume)

    def __str__(self):
        return "fraction = " + str(self.__nume) + "/" + str(self.__denom)


if __name__ == '__main__':
    rat1 = Rational(1, 2)
    rat2 = Rational(3, 4)
    rat3 = rat1 + rat1  # 4/4 = 1
    rat4 = rat3 - rat2  # 4/16 = 1/4
    rat5 = rat2 - rat3  # -4/16 = -1/4
    rat6 = rat1 / rat3  # 4/8 = 1/2
    print(rat6)