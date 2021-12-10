with open('input.txt') as f:
    lines = [x for x in f.read().split('\n') if x != '']

opening = ['(', '[', '{', '<'] 
closing = [')', ']', '}', '>']
match = dict(zip(opening, closing))

corrupted = set()

def part_1():
    points = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
    score = 0
    for line in lines:
        stack = []
        for char in list(line):
            if char in opening: stack.append(char)
            elif char != match[stack.pop()]:
                score += points[char]
                corrupted.add(line)
                break
    return score


def part_2():
    points = { ')': 1, ']': 2, '}': 3, '>': 4 }
    scores = []
    for line in lines:
        if line in corrupted: continue

        stack = []
        for char in list(line):
            if char in opening: stack.append(char)
            else: stack.pop()

        line_score = 0
        for char in stack[::-1]:
            line_score = 5*line_score + points[match[char]]
        scores.append(line_score)

    return sorted(scores)[len(scores)//2]


print("--- PART 1 ---")
print(part_1())
print("--- PART 2 ---")
print(part_2())

