import re

with open('input.txt') as f:
    TARGET_AREA_PATTERN = "target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)"
    TARGET = [int(x) for x in re.match(TARGET_AREA_PATTERN, f.read().strip()).groups()]
    X_FROM, X_TO, Y_FROM, Y_TO = TARGET
    triangular_number = 0
    for i in range(X_FROM):
        triangular_number += i
        if triangular_number >= X_FROM: 
            MIN_X_VELOCITY = i
            break

def project(x_vel, y_vel):
    """ return true if projectile hits within target """
    x_pos, y_pos = 0, 0
    while x_pos <= X_TO and y_pos >= Y_FROM:
        if x_pos >= X_FROM and y_pos <= Y_TO: return True
        x_pos += x_vel
        y_pos += y_vel
        y_vel -= 1
        if x_vel != 0: x_vel -= 1  # x velocity should always be greater than 0
    return False

def part_1():
    for y in range(X_TO, 0, -1):
        for x in range(MIN_X_VELOCITY, X_TO + 1):
            if project(x, y): return y*(y+1)//2

def part_2():
    count = 0
    for x in range(MIN_X_VELOCITY, X_TO + 1):
        for y in range(Y_FROM, X_TO):
            if project(x, y): count += 1
    return count


print("PART 1: ", part_1())
print("PART 2: ", part_2())

