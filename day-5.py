import re

def parse_line(line):
    LINES_REGEX_PATTERN = "(\d+),(\d+) -> (\d+),(\d+)"
    match = re.match(LINES_REGEX_PATTERN, line)
    return [int(x) for x in match.groups()]

# process input 
with open('input.txt') as f:
    lines = [x for x in f.read().split('\n') if x != '']
lines = [parse_line(line) for line in lines]

MAX_SIZE = 1000

def part_1():
    intersections = [[0]*MAX_SIZE for _ in range(MAX_SIZE)]
    for from_x, from_y, to_x, to_y in lines:
        if from_x == to_x:
            for y in range(min(from_y, to_y), max(from_y, to_y) + 1): intersections[from_x][y] += 1
        elif from_y == to_y:
            for x in range(min(from_x, to_x), max(from_x, to_x) + 1): intersections[x][from_y] += 1
    ans = 0
    for row in intersections: ans += len([val for val in row if val > 1])
    return ans

def part_2():
    intersections = [[0]*MAX_SIZE for _ in range(MAX_SIZE)]
    for from_x, from_y, to_x, to_y in lines:
        if from_x == to_x:
            for y in range(min(from_y, to_y), max(from_y, to_y) + 1): intersections[from_x][y] += 1
        elif from_y == to_y:
            for x in range(min(from_x, to_x), max(from_x, to_x) + 1): intersections[x][from_y] += 1
        elif abs(from_x - to_x) == abs(from_y - to_y):
            delta_x = 1 if from_x < to_x else -1
            delta_y = 1 if from_y < to_y else -1
            x,y = from_x, from_y
            for _ in range(abs(from_x - to_x) + 1):
                intersections[x][y] += 1
                x += delta_x
                y += delta_y
    ans = 0
    for row in intersections: ans += len([val for val in row if val > 1])
    return ans

print("PART 1: ", part_1())
print("PART 2: ", part_2())

