with open('input.txt') as f:
    numbers = [int(x) for x in f.read().split(',') if x != '']

MEMO = [None] * 257
def fish(days_left):
    """ returns the number of additional fish spawned; fish should be at a spawning day """
    if days_left < 1: return 0
    if MEMO[days_left] != None: return MEMO[days_left]
    MEMO[days_left] = 1 + fish(days_left - 9) + fish(days_left - 7)
    return MEMO[days_left]

def count_fish(days):
    total = len(numbers)
    for f in numbers: total += fish(days - f)
    return total

def part_1():
    return count_fish(80)

def part_2():
    return count_fish(256)

print("PART 1: ", print(part_1()))
print("PART 2: ", print(part_2()))

