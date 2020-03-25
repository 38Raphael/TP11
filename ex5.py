import numpy as np


class Matrice:
    def __init__(self, d):
        if len(d) == 4:
            self.__data = np.array([[d[0], d[1]], [d[2], d[3]]])
        else:
            print("Choisissez une liste de quatre nombres entiers")

    def __add__(self, other):
        if isinstance(other, Matrice):
            return Matrice([self.__data[0][0] + other.__data[0][0], self.__data[0][1] + other.__data[0][1],
                            self.__data[1][0] + other.__data[1][0], self.__data[1][1] + other.__data[1][1]])

    def __iadd__(self, other):
        if isinstance(other, Matrice):
            self.__data[0][0] += other.__data[0][0]
            self.__data[0][1] += other.__data[0][1]
            self.__data[1][0] += other.__data[1][0]
            self.__data[1][1] += other.__data[1][1]
            return self.__data

    def __sub__(self, other):
        if isinstance(other, Matrice):
            return Matrice([self.__data[0][0] - other.__data[0][0], self.__data[0][1] - other.__data[0][1],
                            self.__data[1][0] - other.__data[1][0], self.__data[1][1] - other.__data[1][1]])

    def __isub__(self, other):
        if isinstance(other, Matrice):
            self.__data[0][0] -= other.__data[0][0]
            self.__data[0][1] -= other.__data[0][1]
            self.__data[1][0] -= other.__data[1][0]
            self.__data[1][1] -= other.__data[1][1]
            return self.__data

    def __mul__(self, other):
        if isinstance(other, Matrice):
            return Matrice([self.__data[0][0] * other.__data[0][0] + self.__data[0][1] * other.__data[1][0],
                            self.__data[0][0] * other.__data[0][1] + self.__data[0][1] * other.__data[1][1],
                            self.__data[1][0] * other.__data[0][0] + self.__data[1][1] * other.__data[1][0],
                            self.__data[1][0] * other.__data[0][1] + self.__data[1][1] * other.__data[1][1]])

    def __imul__(self, other):
        if isinstance(other, Matrice):
            self.__data = np.array([[self.__data[0][0] * other.__data[0][0] + self.__data[0][1] * other.__data[1][0],
                                     self.__data[0][0] * other.__data[0][1] + self.__data[0][1] * other.__data[1][1]],
                                    [self.__data[1][0] * other.__data[0][0] + self.__data[1][1] * other.__data[1][0],
                                     self.__data[1][0] * other.__data[0][1] + self.__data[1][1] * other.__data[1][1]]])
            return self.__data

    def __lt__(self, other):
        if isinstance(other, Matrice):
            return self.__data < other.__data

    def __gt__(self, other):
        if isinstance(other, Matrice):
            return self.__data > other.__data

    def __str__(self):
        return "matrice =\n" + str(self.__data)


if __name__ == '__main__':
    mat1 = Matrice([1, 1, 1, 1])
    mat2 = Matrice([0, 1, 0, 1])
    print(mat1)
    mat3 = mat1 < mat2
    print(mat3)
    print(mat1 + mat2)
    mat4 = mat1 * mat2
    mat1 *= mat2
    print(mat4)
    print(mat1)
