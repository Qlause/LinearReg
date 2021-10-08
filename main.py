class LinearReg:
    def __init__(self, x_value, y_value):
        self.__x, self.__y = x_value, y_value
        self.__xy, self.__x2, self.__value = [], [], []
        self.__sigx, self.__sigy, self.__sigxy, self.__sigx2 = float(0), float(0), float(0), float(0)

        self.get_all_value()

    def get_all_value(self):
        for i in range(0, len(self.__x)):
            self.__xy.append(self.__x[i] * self.__y[i])
            self.__x2.append(self.__x[i] ** 2)
            self.__sigx += self.__x[i]
            self.__sigy += self.__y[i]
            self.__sigxy += self.__xy[i]
            self.__sigx2 += self.__x2[i]

    def slope(self):

        slope1 = len(self.__x) * self.__sigxy - self.__sigx * self.__sigy
        slope2 = len(self.__x) * self.__sigx2 - self.__sigx ** 2
        slope = slope1 / slope2

        return slope

    def intercept(self):

        y_intercept1 = self.__sigy - self.slope() * self.__sigx
        y_intercept = y_intercept1 / len(self.__x)

        return y_intercept

    def getwvar(self, gety):
        return self.intercept() + (self.slope() * gety)


a = [1, 2, 3]
b = [4, 5, 6]

test = LinearReg(a, b)

print(test.getwvar(5))
