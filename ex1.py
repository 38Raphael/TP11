class Cercle:
    def __init__(self, r):
        self.__rayon = r

    def __add__(self, other):
        if isinstance(other, Cercle) == True:
            return Cercle(self.__rayon + other.__rayon)

    def __lt__(self, other):
        if isinstance(other, Cercle) == True:
            return self.__rayon < other.__rayon

    def __gt__(self, other):
        if isinstance(other, Cercle) == True:
            return self.__rayon > other.__rayon

    def __str__(self):
        return "Rayon du cercle: r=" + str(self.__rayon)

if __name__ == '__main__':
    c1 = Cercle(2)
    c2 = Cercle(3)
    c3 = c1 + c2
    c4 = c1 < c2
    c5 = c2 > c3
    print(c3)