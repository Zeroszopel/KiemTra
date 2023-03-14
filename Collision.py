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

