from collections import Counter

with open('input.txt') as f:
    polymer, rules = f.read().strip().split('\n\n')
    rules = dict([((p[0], p[1]), b) for p, b in [x.split(' -> ') for x in rules.split('\n')]])
    polymer = list(polymer)

MEMO = [{} for _ in range(41)]
MEMO[1] = dict(zip(rules.keys(), [Counter([x]) for x in rules.values()]))

def expand(pair, n):
    """ returns the counter of letters BETWEEN the pair after expansion """
    if pair not in MEMO[n]:
        mid = rules[pair]
        MEMO[n][pair] = expand((pair[0], mid), n - 1) + expand(pair, 1) + expand((mid, pair[1]), n - 1)
    return MEMO[n][pair]

def step(num_steps):
    counts = Counter(polymer)
    for i in range(len(polymer) - 1):
        counts += expand((polymer[i], polymer[i + 1]), num_steps)
    return max(counts.values()) - min(counts.values())

def part_1():
    return step(10)

def part_2():
    return step(40)


print("PART 1: ", part_1())
print("PART 2: ", part_2())

