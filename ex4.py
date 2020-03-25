class Duree:
    def __init__(self, h, m, s):
        self.__heure = h
        self.__minute = m
        self.__seconde = s

    def affduree(self):
        if self.__heure >= 0 and self.__minute >= 0 and self.__seconde >= 0:
            if self.__seconde < 60:
                if self.__minute < 60:
                    if self.__heure < 24:
                        return str(self.__heure) + "h" + str(self.__minute) + "m" + str(self.__seconde) + "s"
                    else:
                        while self.__heure > 24:
                            self.__heure -= 24
                        return str(self.__heure) + "h" + str(self.__minute) + "m" + str(self.__seconde) + "s"
                else:
                    while self.__minute > 60:
                        self.__minute -= 60
                        self.__heure += 1
                    if self.__heure < 24:
                        return str(self.__heure) + "h" + str(self.__minute) + "m" + str(self.__seconde) + "s"
                    else:
                        while self.__heure > 24:
                            self.__heure -= 24
                        return str(self.__heure) + "h" + str(self.__minute) + "m" + str(self.__seconde) + "s"
            else:
                while self.__seconde > 60:
                    self.__seconde -= 60
                    self.__minute += 1
                if self.__minute < 60:
                    if self.__heure < 24:
                        return str(self.__heure) + "h" + str(self.__minute) + "m" + str(self.__seconde) + "s"
                    else:
                        while self.__heure > 24:
                            self.__heure -= 24
                        return str(self.__heure) + "h" + str(self.__minute) + "m" + str(self.__seconde) + "s"
                else:
                    while self.__minute > 60:
                        self.__minute -= 60
                        self.__heure += 1
                    if self.__heure < 24:
                        return str(self.__heure) + "h" + str(self.__minute) + "m" + str(self.__seconde) + "s"
                    else:
                        while self.__heure > 24:
                            self.__heure -= 24
                        return str(self.__heure) + "h" + str(self.__minute) + "m" + str(self.__seconde) + "s"
        else:
            return "Choisissez une heure, des minutes et des secondes positives"

    def __add__(self, other):
        if isinstance(other, Duree):
            return Duree(self.__heure + other.__heure, self.__minute + other.__minute, self.__seconde + other.__seconde)


if __name__ == '__main__':
    h1 = Duree(25, 360, 74)
    h2 = Duree(52, 82, 21)
    print(h1.affduree())
    print(h2.affduree())
    h3 = h1 + h2
    print(h3.affduree())
