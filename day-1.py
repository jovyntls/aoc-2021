with open('input.txt') as f:
    numbers = [int(x) for x in f.read().split('\n') if x != '']

def part_1():
    ans = 0
    for (i, n) in enumerate(numbers[1:]):
        if n > numbers[i]: ans += 1
    return ans

def part_2():
    ans = 0
    for i in range(len(numbers) - 3):
      if numbers[i] < numbers[i+3]: ans += 1
    return ans

print("PART 1: ", part_1())
print("PART 2: ", part_2())

