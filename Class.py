from abc import ABC, abstractmethod
import math

#Bài 2
class Shape:
    @abstractmethod
    def printinfo(self):
        pass

    @abstractmethod
    def chuVi(self):
        pass

    @abstractmethod
    def dienTich(self):
        pass

#Bài 3
class Rect(Shape):
    def __init__(self, rong, dai, x, y, ):
        self.Rong = rong
        self.Dai = dai
        self.X = x
        self.Y = y
        self.ChuVi = self.chuVi()
        self.DienTich = self.dienTich()

    def printinfo(self):
        print("#Rectangle")
        print("Chiều rộng:{} Chiều dài:{}".format(self.Rong, self.Dai))
        print("Tọa độ: ({}, {})".format(self.X, self.Y))

    def chuVi(self):
        ChuVi = (self.Rong + self.Dai) * 2
        return ChuVi

    def dienTich(self):
        DienTich = self.Rong * self.Dai
        return DienTich


class Circle(Shape):
    def __init__(self, bk, x, y, ):
        self.BK = bk
        self.X = x
        self.Y = y
        self.ChuVi = self.chuVi()
        self.DienTich = self.dienTich()

    def printinfo(self):
        print("#Circle")
        print("Bán kính:{}".format(self.BK))
        print("Tọa độ: ({}, {})".format(self.X, self.Y))

    def chuVi(self):
        ChuVi = self.BK * 2 * 3.14
        return ChuVi

    def dienTich(self):
        DienTich = pow(self.BK, 2) * 3.14
        return DienTich


class Triangle(Shape):
    def __init__(self, a, b, c, x, y, ):
        self.A = a
        self.B = b
        self.C = c
        self.X = x
        self.Y = y
        self.ChuVi = self.chuVi()
        self.DienTich = self.dienTich()

    def printinfo(self):
        print("#Triangle")
        print("Cạnh A:{} Cạnh B:{} Cạnh C:{}".format(self.A, self.B, self.C))
        print("Tọa độ: ({}, {})".format(self.X, self.Y))

    def chuVi(self):
        ChuVi = self.A + self.B + self.C
        return ChuVi

    def dienTich(self):
        p = self.ChuVi / 2
        DienTich = math.sqrt(p * (p - self.A) * (p - self.B) * (p - self.C))
        return DienTich
