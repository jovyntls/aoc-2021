from collections import Counter

with open('input.txt') as f:
    lines = [x for x in f.read().split('\n') if x != '']


def part_1():
    print("--- PART 1 ---")

    baseline = len(lines) // 2
    bit_counts = [0] * len(lines[0])
    for line in lines:
        for (i, b) in enumerate(line):
            if b == '1': bit_counts[i] += 1
    most_common = "".join(['1' if x > baseline else '0' for x in bit_counts])
    least_common = "".join(['0' if x > baseline else '1' for x in bit_counts])

    print('ans: ', int(most_common, 2) * int(least_common, 2))


def part_2():
    print("--- PART 2 ---")

    numbers = lines
    for index in range(len(numbers[0])):
        bit_counter = Counter([num[index] for num in numbers])
        more_common = '1' if bit_counter['1'] >= bit_counter['0'] else '0'
        numbers = [x for x in numbers if x[index] == more_common]
        if len(numbers) == 1: break
    oxygen_generator_rating = int(numbers.pop(), 2)
    print("oxygen_generator_rating: ", oxygen_generator_rating)

    numbers = lines
    for index in range(len(numbers[0])):
        bit_counter = Counter([num[index] for num in numbers])
        less_common = '1' if bit_counter['1'] < bit_counter['0'] else '0'
        numbers = [x for x in numbers if x[index] == less_common]
        if len(numbers) == 1: break
    co2_scrubber_rating = int(numbers.pop(), 2)
    print("co2_scrubber_rating: ", co2_scrubber_rating)

    print('ans: ', co2_scrubber_rating * oxygen_generator_rating)


part_1()
part_2()

