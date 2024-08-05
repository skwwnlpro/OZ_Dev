import math

# 삼각형의 넓이
def triangle(a, b):
    return a * b * 1/2

# 원의 넓이
def circle(a):
    return math.pi * a**2

# 직육면체의 표면적
def rectangular(a, b, c):
    return 2 * (a * b + a * c + b * c)