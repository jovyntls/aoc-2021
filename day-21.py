from collections import Counter
from itertools import product

PERMUTATIONS = Counter([sum(x) for x in list(product((1,2,3), repeat=3))]).items()
MEMO = {}

with open('input.txt') as f:
    starting_positions = [int(x[-1]) for x in f.read().strip().split('\n')]

def play(p1, p2, s1, s2):
    if (p1, p2, s1, s2) not in MEMO:
        wins = (0,0)
        for (roll, occurrence) in PERMUTATIONS:
            moved = (p1+roll-1) % 10 + 1
            if s1 + moved >= 21: 
                wins = (wins[0] + occurrence, wins[1])
                continue
            next_game = play(p2, moved, s2, s1 + moved)
            wins = (wins[0] + occurrence*next_game[1], wins[1] + occurrence*next_game[0])
        MEMO[(p1, p2, s1, s2)] = wins
    return MEMO[(p1, p2, s1, s2)]


def part_1():
    p1, p2 = starting_positions
    s1, s2 = 0, 0
    d = 1
    num_rolls = 0
    while s1 < 1000 and s2 < 1000:
        total_roll = sum(range(d, d+3))
        num_rolls += 3
        d = (d+2)%100 + 1
        p1 = (p1+total_roll-1) % 10 + 1
        s1 += p1
        p1, p2 = p2, p1
        s1, s2 = s2, s1
    return num_rolls * min(s1, s2)

def part_2():
    p1, p2 = starting_positions
    return max(play(p1,p2,0,0))


print("PART 1: ", part_1())
print("PART 2: ", part_2())

