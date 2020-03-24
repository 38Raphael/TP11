class Complex:
    def __init__(self, re, im):
        self.__reel = re
        self.__imag = im

    def __add__(self, other):
        if isinstance(other, Complex) is True:
            return Complex(self.__reel + other.__reel, self.__imag + other.__imag)

    def __sub__(self, other):
        if isinstance(other, Complex) is True:
            return Complex(self.__reel - other.__reel, self.__imag - other.__imag)

    def __mul__(self, other):
        if isinstance(other, Complex) is True:
            return Complex(self.__reel * other.__reel - self.__imag * self.__imag, 2 * (self.__imag * other.__imag))

    def __truediv__(self, other):
        if isinstance(other, Complex) is True:
            return Complex((self.__reel * other.__reel + self.__imag * other.__imag)/(other.__reel**2 - other.__imag**2), (self.__imag * other.__imag - self.__reel * other.__imag)/(other.__reel**2 - other.__imag**2))

    def __abs__(self):
        return (self.__reel**2+self.__imag**2)**0.5

    def __eq__(self, other):
        if isinstance(other, Complex) is True:
            return self.__reel == other.__reel and self.__imag == other.__imag

    def __ne__(self, other):
        if isinstance(other, Complex) is True:
            return self.__reel != other.__reel and self.__imag != other.__imag

    def __str__(self):
        return "partie réelle =" + str(self.__reel) + " et partie imaginaire =" + str(self.__imag)



if __name__ == '__main__':
    comp1 = Complex(1, 2)
    comp2 = Complex(2, 3)
    comp3 = comp1 + comp2
    comp4 = comp2 - comp1
    comp5 = comp1 * comp3
    comp6 = comp3 / comp3
    comp7 = comp3 == comp3
    comp8 = comp1 != comp4
    comp9 = abs(comp4)
    print(comp6)