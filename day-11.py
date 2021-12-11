with open('input.txt') as f:
    octopi = [[int(y) for y in list(x)] for x in f.read().split('\n') if x != '']

class Grid:
    def __init__(self, octopi):
        self.octopi = [row.copy() for row in octopi]
        self.nrows, self.ncols = len(octopi), len(octopi[0])
        self.flashes = 0

    def step(self):
        self.flashed = [[False] * self.ncols for _ in range(self.nrows)]
        for r in range(self.nrows):
            for c in range(self.ncols):
                self.increment(r, c)
        self.flashes += sum([row.count(True) for row in self.flashed])

    def flash(self, r, c):
        self.flashed[r][c] = True
        self.octopi[r][c] = 0
        for x in [r-1, r, r+1]:
            for y in [c-1, c, c+1]:
                self.increment(x, y)
    
    def increment(self, r, c):
        if r < 0 or c < 0 or r >= self.nrows or c >= self.ncols: return
        if self.flashed[r][c]: return
        self.octopi[r][c] += 1
        if self.octopi[r][c] > 9: self.flash(r, c)

        
def part_1():
    grid = Grid(octopi)
    for _ in range(100): grid.step()
    return grid.flashes

def part_2():
    grid = Grid(octopi)
    num_octopi = grid.nrows * grid.ncols
    i = 1
    while True:
        grid.step()
        if sum([row.count(0) for row in grid.octopi]) == num_octopi: return i
        i += 1


print("PART 1: ", print(part_1()))
print("PART 2: ", print(part_2()))

