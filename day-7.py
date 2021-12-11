import sys

sys.setrecursionlimit(1500)  # else triangle(n) exceeds maximum recursion limit

with open('input.txt') as f:
    numbers = [int(x) for x in f.read().split(',') if x != '']

MEMO = {0: 0}
def triangle(n):
    if n not in MEMO: MEMO[n] = n + triangle(n-1)
    return MEMO[n]

def part_1():
    sums = [sum([abs(m-n) for m in numbers]) for n in numbers]
    return min(sums)

def part_2():
    sums = [sum([triangle(abs(m-n)) for m in numbers]) for n in range(min(numbers), max(numbers) + 1)]
    return min(sums)


print("PART 1: ", print(part_1()))
print("PART 2: ", print(part_2()))

