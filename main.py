
year_e = [1.1, 1.3, 1.5, 2, 2.2,
          2.9, 3, 3.2, 3.2, 3.7,
          3.9, 4, 4, 4.1, 4.5,
          4.9, 5.1, 5.3, 5.9, 6,
          6.8, 7.1, 7.9, 8.2, 8.7,
          9, 9.5, 9.6, 10.3, 10.5]

salary = [39343, 46205, 37731, 43525, 39891,
          56642, 60150, 54445, 64445, 57189,
          63218, 55794, 56957, 57081, 61111,
          67938, 66029, 83088, 81363, 93940,
          91738, 98273, 101302, 113812, 109431,
          105582, 116969, 112635, 122391, 121872]


class LinearReg:

    # Set Necessary Value
    def __init__(self, x_value, y_value):
        self.__x, self.__y = x_value, y_value
        self.__xy, self.__x2, self.__value = [], [], []
        self.__sigx, self.__sigy, self.__sigxy, self.__sigx2 = float(0), float(0), float(0), float(0)

        if len(self.__x) == len(self.__y):
            for i in range(0, len(self.__x)):
                self.__xy.append(self.__x[i] * self.__y[i])
                self.__x2.append(self.__x[i] ** 2)
                self.__sigx += self.__x[i]
                self.__sigy += self.__y[i]
                self.__sigxy += self.__xy[i]
                self.__sigx2 += self.__x2[i]

        else:
            print("x and y do not have same value, value can not be set")

    # =============== #
    #  Function here  #
    # =============== #

    # Get Slope Value
    def get_slope(self):

        try:
            slope1 = len(self.__x) * self.__sigxy - self.__sigx * self.__sigy
            slope2 = len(self.__x) * self.__sigx2 - self.__sigx ** 2
            slope = slope1 / slope2

            return slope

        except ValueError as e:
            return print('data load error', e)

    # Get Intercept Value
    def get_intercept(self):

        try:
            y_intercept1 = self.__sigy - self.get_slope() * self.__sigx
            y_intercept = y_intercept1 / len(self.__x)

            return y_intercept

        except ValueError as e:
            return print('data load error', e)

    # Get Dependent Value
    def getvar_value(self, gety):
        try:
            return self.get_intercept() + (self.get_slope() * gety)

        except ValueError as e:
            return print('data load error', e)


test = LinearReg(year_e, salary)
print(test.getwvar(5))
