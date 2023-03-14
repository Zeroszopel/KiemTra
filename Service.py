import random
from Class import Triangle, Rect, Circle
from Collision import isCirclesColliding, isRectanglesColliding, Collision
import time
rec = []
tri = []
cir = []
size = 11
array = []
check = []

def generateRec(f):
    a = random.randint(0, 20)
    b = random.randint(0, 20)
    if a > b:
        c = a
        a = b
        b = c
    x = random.randint(-50, 50)
    y = random.randint(-50, 50)
    f.write("#Rect\n")
    f.write("{} {}\n".format(a, b))
    f.write("{} {}\n".format(x, y))


def generateCir(f):
    bk = random.randint(0, 10)
    x = random.randint(-50, 50)
    y = random.randint(-50, 50)
    f.write("#Circle\n")
    f.write("{}\n".format(bk))
    f.write("{} {}\n".format(x, y))


def generateTri(f):
    a, b, c = 0, 0, 0
    while a + b <= c or a + c <= b or \
            b + c <= a:
        a = random.randint(0, 20)
        b = random.randint(0, 20)
        c = random.randint(0, a + b)
    x = random.randint(-50, 50)
    y = random.randint(-50, 50)
    f.write("#Triangle\n")
    f.write("{} {} {}\n".format(a, b, c))
    f.write("{} {}\n".format(x, y))


# Bài 1
def createfile(filename="input.txt", amount=10*10*10):
    global size
    size = amount
    try:
        with open(filename, "w") as f:
            for i in range(amount):
                generateRec(f)
                generateCir(f)
                generateTri(f)
        return True
    except:
        return False


# Bài 4a
def readfile(filename):
    global rec
    global cir
    global tri
    global size
    try:
        with open(filename) as file:
            line = file.readline()
            while line != '':
                if line == "#Rect\n":
                    data = file.readline()
                    data.replace("\n", "")
                    info = [int(x) for x in data.split(" ")]
                    data2 = file.readline()
                    data2.replace("\n", "")
                    info2 = [int(x) for x in data2.split(" ")]
                    rect = Rect(info[0], info[1], info2[0], info2[1])
                    rec.append(rect)
                if line == "#Circle\n":
                    data = file.readline()
                    data.replace("\n", "")
                    info = int(data.strip())
                    data2 = file.readline()
                    data2.replace("\n", "")
                    info2 = [int(x) for x in data2.split(" ")]
                    circle = Circle(info, info2[0], info2[1])
                    cir.append(circle)
                if line == "#Triangle\n":
                    data = file.readline()
                    data.replace("\n", "")
                    info = [int(x) for x in data.split(" ")]
                    data2 = file.readline()
                    data2.replace("\n", "")
                    info2 = [int(x) for x in data2.split(" ")]
                    triangle = Triangle(info[0], info[1], info[2], info2[0], info2[1])
                    tri.append(triangle)
                line = file.readline()
        size = len(rec)
        return True
    except:
        return False


# Bài 4b
def checkmax():
    maxCV = 0
    maxDT = 0
    for i in rec:
        if i.ChuVi > maxCV:
            cv = i
            maxCV = i.ChuVi
            print(maxCV)
        if i.DienTich > maxDT:
            dt = i
            maxDT = i.DienTich
            print(maxDT)
    for i in cir:
        if i.ChuVi > maxCV:
            cv = i
            maxCV = i.ChuVi
            print(maxCV)
        if i.DienTich > maxDT:
            dt = i
            maxDT = i.DienTich
            print(maxDT)
    for i in tri:
        if i.ChuVi > maxCV:
            cv = i
            maxCV = i.ChuVi
            print(maxCV)
        if i.DienTich > maxDT:
            dt = i
            maxDT = i.DienTich
            print(maxDT)
    print("Hình có chu vi lớn nhất với chu vi là {}:".format(maxCV))
    cv.printinfo()
    print("-" * 30)
    print("Hình có diện tích lớn nhất với diện tích là {}:".format(maxDT))
    dt.printinfo()


def getinfo(e):
    if e == 1:
        print("_" * 80)
        print("Danh sách thông tin hình vuông:")
        for i in range(0, len(rec)):
            print("{}. ".format(i + 1), end="")
            rec[i].printinfo()
            print()
    if e == 2:
        print("_" * 80)
        print("Danh sách thông tin hình tròn:")
        for i in range(0, len(cir)):
            print("{}. ".format(i + 1), end="")
            cir[i].printinfo()
            print()
    if e == 3:
        print("_" * 80)
        print("Danh sách thông tin hình tam giác:")
        for i in range(0, len(rec)):
            print("{}. ".format(i + 1), end="")
            rec[i].printinfo()
            print()

def getCollide(x, y, value):
    value += 1
    check[x][y] = False
    check[y][x] = False
    for i in range(0, size*2):
        if array[y][i] == 1 and check[y][i]:
            value = getCollide(y, i, value)
    return value

def arrayinput():
    global array
    count=1
    for indexcir in range(0, len(cir)):
        for indexcir2 in range(indexcir+1, len(cir)):
            rs = isCirclesColliding(cir[indexcir], cir[indexcir2])
            if rs:
                array[indexcir][indexcir2] = 1
                array[indexcir2][indexcir] = 1

    for indexrec in range(0, len(rec)):
        for indexrec2 in range(indexrec+1, len(rec)):
            rs = isRectanglesColliding(rec[indexrec], rec[indexrec2])
            if rs:
                array[size + indexrec][size + indexrec2] = 1
                array[size + indexrec2][size + indexrec] = 1

    for indexcir in range(0, len(cir)):
        for indexrec in range(0, len(rec)):
            c = cir[indexcir]
            r = rec[indexrec]
            rs = Collision(c.X, c.Y, c.BK, r.X, r.Y, r.Dai, r.Rong)
            if rs:
                array[indexcir][size + indexrec] = 1
                array[size + indexrec][indexcir] = 1
def getcollidemax():
    global maxstring
    global stri
    maximum = 0
    for i in range(0, size * 2):
        for j in range(0, size * 2):
            if array[i][j] == 1 and check[i][j]:
                data = getCollide(i, j, 1)
                if data > maximum:
                    maximum = data
    print("Số hình chồng lên nhiều nhất là {}".format(maximum))


def createarray():
    global array
    global check
    global check2
    for i in range(0, size*2):
        ar1 = []
        for j in range(0, size*2):
            ar1.append(0)
        array.append(ar1)
    for i in range(0, size*2):
        ar1 = []
        for j in range(0, size*2):
            ar1.append(True)
        check.append(ar1)
