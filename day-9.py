with open('input.txt') as f:
    numbers = [[int(y) for y in list(x)] for x in f.read().split('\n') if x != '']

lows = []
def part_1():
    risk = 0
    for r, row in enumerate(numbers):
        for c, n in enumerate(row):
            if c > 0 and numbers[r][c-1] <= n: continue
            if c < len(row) - 1 and numbers[r][c+1] <= n: continue
            if r > 0 and numbers[r-1][c] <= n: continue
            if r < len(numbers) - 1 and numbers[r+1][c] <= n: continue
            risk += 1 + n
            lows.append((r, c))
    return risk

def part_2():
    visited = [[False for _ in numbers[0]] for _ in numbers]
    nrows, ncols = len(numbers), len(numbers[0])
    
    def basin(r, c):
        if c < 0 or r < 0 or c >= ncols or r >= nrows or visited[r][c] or numbers[r][c] == 9: return 0
        n = numbers[r][c]
        visited[r][c] = True
        return 1 + basin(r, c-1) + basin(r, c+1) + basin(r-1, c) + basin(r+1, c)

    basins = sorted([basin(*l) for l in lows], reverse=True)
    return basins[0] * basins[1] * basins[2]


print("PART 1: ", part_1())
print("PART 2: ", part_2())

