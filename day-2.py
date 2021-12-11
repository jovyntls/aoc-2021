with open('input.txt') as f:
    lines = [x.split(" ") for x in f.read().split('\n') if x != '']
    lines = [(x, int(y)) for x, y in lines]

def part_1():
    depth, horizontal = 0, 0
    for inst, magnitude in lines:
      if inst == 'down': depth += magnitude
      elif inst == 'up': depth -= magnitude
      elif inst == 'forward': horizontal += magnitude
    return depth * horizontal

def part_2():
    depth = horizontal = aim = 0
    for inst, magnitude in lines:
      if inst == 'down': aim += magnitude
      elif inst == 'up': aim -= magnitude
      elif inst == 'forward':
        horizontal += magnitude
        depth += aim * magnitude
    return depth * horizontal


print("PART 1: ", part_1())
print("PART 2: ", part_2())

