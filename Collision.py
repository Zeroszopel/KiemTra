import math


def isCirclesColliding(cir1, cir2):
    sidea = abs(cir1.X - cir2.X)
    sideb = abs(cir1.Y - cir2.Y)
    distance = math.sqrt(pow(sidea, 2) + pow(sideb, 2))
    if distance < (cir1.BK + cir2.BK):
        return True
    return False


def isRectanglesColliding(rec1, rec2):
    top1 = rec1.Y + rec1.Rong
    right1 = rec1.X + rec1.Dai
    left1 = rec1.X
    bottom1 = rec1.Y
    top2 = rec2.Y + rec2.Rong
    right2 = rec2.X + rec2.Dai
    left2 = rec2.X
    bottom2 = rec2.Y
    if left1 < right2 and right1 > left2 and bottom1 < top2 and top1 > bottom2:
        return True
    return False


def testForCollision(circleX, circleY, width, height, radius):
    dx = min(circleX, (width * 0.5))
    dx1 = max(dx, (-width * 0.5))

    dy = min(circleY, (height * 0.5))
    dy1 = max(dy, (-height * 0.5))

    return (dx1 - circleX) * (dx1 - circleX) + (dy1 - circleY) * (dy1 - circleY) <= radius * radius


def Collision(circleX, circleY, radius, squareX, squareY, width, height):
    center_of_square_x = squareX + width / 2
    center_of_square_y = squareY + height / 2

    if center_of_square_x == 0 and center_of_square_y == 0:

        return testForCollision(circleX, circleY, width, height, radius)

    else:
        circleX = circleX - center_of_square_x
        circleY = circleY - center_of_square_y
        return testForCollision(circleX, circleY, width, height, radius)


def isnotTriangleCollision(point1, point2):
    dxa = point1[0][0] - point2[2][0]
    dya = point1[0][1] - point2[2][1]
    dxb = point1[1][0] - point2[2][0]
    dyb = point1[1][1] - point2[2][1]
    dxc = point1[2][0] - point2[2][0]
    dyc = point1[2][1] - point2[2][1]
    dx21 = point2[2][0] - point2[1][0]
    dy12 = point2[1][1] - point2[2][1]
    D = dy12 * (point2[0][0] - point2[2][0]) + dx21 * (point2[0][1] - point2[2][1])
    sa = dy12 * dxa + dx21 * dya
    sb = dy12 * dxb + dx21 * dyb
    sc = dy12 * dxc + dx21 * dyc
    ta = (point2[2][1] - point2[0][1]) * dxa + (point2[0][0] - point2[2][0]) * dya
    tb = (point2[2][1] - point2[0][1]) * dxb + (point2[0][0] - point2[2][0]) * dyb
    tc = (point2[2][1] - point2[0][1]) * dxc + (point2[0][0] - point2[2][0]) * dyc
    if D < 0:
        return ((sa >= 0 and sb >= 0 and sc >= 0) or (ta >= 0 and tb >= 0 and tc >= 0) or
                (sa + ta <= D and sb + tb <= D and sc + tc <= D))
    return ((sa <= 0 and sb <= 0 and sc <= 0) or (ta <= 0 and tb <= 0 and tc <= 0) or
            (sa + ta >= D and sb + tb >= D and sc + tc >= D))


def CircleTriangleCollision(point, circle):
    v1x, v1y, v2x, v2y, v3x, v3y = point[0][0], point[0][1], point[1][0], point[1][1], point[2][0], point[2][1]
    centrex, centrey, radius = circle.X, circle.Y, circle.BK
    c1x = centrex - v1x
    c1y = centrey - v1y
    radiusSqr = radius * radius
    c1sqr = c1x * c1x + c1y * c1y - radiusSqr
    if c1sqr <= 0:
        return True

    c2x = centrex - v2x
    c2y = centrey - v2y
    c2sqr = c2x * c2x + c2y * c2y - radiusSqr
    if c2sqr <= 0:
        return True

    c3x = centrex - v3x
    c3y = centrey - v3y
    c3sqr = c3x * c3x + c3y * c3y - radiusSqr
    if c3sqr <= 0:
        return True

    e1x = v2x - v1x
    e1y = v2y - v1y
    e2x = v3x - v2x
    e2y = v3y - v2y
    e3x = v1x - v3x
    e3y = v1y - v3y
    if (e1y * c1x >= e1x * c1y) and (e2y * c2x >= e2x * c2y) and (e3y * c3x >= e3x * c3y):
        return True

    k = c1x * e1x + c1y * e1y
    if k > 0:
        len = e1x * e1x + e1y * e1y
        if k < len:
            if c1sqr * len <= k * k:
                return True

    k = c2x * e2x + c2y * e2y
    if k > 0:
        len = e2x * e2x + e2y * e2y
        if k < len:
            if c2sqr * len <= k * k:
                return True

    k = c3x * e3x + c3y * e3y
    if k > 0:
        len = e3x * e3x + e3y * e3y
        if k < len:
            if c3sqr * len <= k * k:
                return True
    return False


def getarea(a, b, c):
    area = (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
    return abs(area)


def isInsideTriangle(point, P):
    areaOfABC = getarea(point[0], point[1], point[2])
    areaOfPAB = getarea(P, point[0], point[1])
    areaOfPBC = getarea(P, point[1], point[2])
    areaOfPCA = getarea(P, point[2], point[0])
    return areaOfABC == areaOfPAB + areaOfPBC + areaOfPCA


def TriangleRectangleCollision(point, rec):
    v1x, v1y, v2x, v2y, v3x, v3y = point[0][0], point[0][1], point[1][0], point[1][1], point[2][0], point[2][1]
    top = rec.Y + rec.Rong
    right = rec.X + rec.Dai
    left = rec.X
    bottom = rec.Y
    if left <= v1x <= right and bottom <= v1y <= top:
        return True
    if left <= v2x <= right and bottom <= v2y <= top:
        return True
    if left <= v3x <= right and bottom <= v3y <= top:
        return True
    if isInsideTriangle(point, [top, left]):
        return True
    if isInsideTriangle(point, [top, right]):
        return True
    if isInsideTriangle(point, [bottom, left]):
        return True
    if isInsideTriangle(point, [bottom, right]):
        return True
    return False
