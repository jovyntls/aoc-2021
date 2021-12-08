from collections import Counter

with open('input.txt') as f:
    lines = [[y.split(' ') for y in x.split(' | ')] for x in f.read().split('\n') if x != '']

SIGNALS = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9'
}

def resolve(digits):
    maps = {}
    lens = [len(d) for d in digits]
    counts = Counter(''.join(digits))
    k_by_v = lambda v: list(counts.keys())[list(counts.values()).index(v)]
    maps['e'] = k_by_v(4)
    maps['b'] = k_by_v(6)
    maps['f'] = k_by_v(9)
    d1 = digits[lens.index(2)]
    maps['c'] = d1[0] if d1[0] != maps['f'] else d1[1]
    maps['a'] = [k for k in counts.keys() if counts[k] == 8 and k != maps['c']][0]
    maps['d'] = set(list(digits[lens.index(4)])).intersection(set(k for k in counts.keys() if counts[k] == 7)).pop()
    maps['g'] = set(list('abcdefg')).difference(maps.values()).pop()
    return dict(zip(maps.values(), maps.keys()))

def chars_to_number(chars, maps):
    return ''.join(sorted([maps[c] for c in chars]))


def part_1():
    counted = {2,3,4,7}
    return sum([len([len(num) for num in output if len(num) in counted]) for (_, output) in lines])

def part_2():
    ans = 0
    for (digits, output) in lines:
        digit_map = resolve(digits)
        converted_output = ''.join([SIGNALS[chars_to_number(chars, digit_map)] for chars in output])
        ans += int(converted_output)
    return ans


print("PART 1: ", part_1())
print("PART 2: ", part_2())

