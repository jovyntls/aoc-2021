import heapq as hq

with open('input.txt') as f:
    map_tile = [[int(y) for y in list(x)] for x in f.read().strip().split('\n')]

def shortest_path(weights, end_row, end_col):
    pq = [(0, (0, 0))]
    visited = [[False]*(end_col+1) for _ in range(end_row+1)]
    while True:
        (path_len, (x, y)) = hq.heappop(pq)
        if visited[x][y]: continue
        if x == end_row and y == end_col: return path_len
        visited[x][y] = True
        if x - 1 > 0 and not visited[x-1][y]: hq.heappush(pq, (path_len + weights[x-1][y], (x-1, y)))
        if x + 1 <= end_row and not visited[x+1][y]: hq.heappush(pq, (path_len + weights[x+1][y], (x+1, y)))
        if y - 1 > 0 and not visited[x][y-1]: hq.heappush(pq, (path_len + weights[x][y-1], (x, y-1)))
        if y + 1 <= end_col and not visited[x][y+1]: hq.heappush(pq, (path_len + weights[x][y+1], (x, y+1)))


def part_1():
    end_row, end_col = len(map_tile) - 1, len(map_tile[0]) - 1
    return shortest_path(map_tile, end_row, end_col)

def part_2():
    map_full = [[] for _ in map_tile]
    for i in range(5):
        next_tile = [[(x+i-1)%9 + 1 for x in row] for row in map_tile]
        map_full = [curr_row + right_col for curr_row, right_col in zip(map_full, next_tile)]
    for i in range(1, 5):
        map_full += [[(x+i-1)%9 + 1 for x in row] for row in map_full[:len(map_tile)]] 
    end_row, end_col = len(map_full) - 1, len(map_full[0]) - 1
    return shortest_path(map_full, end_row, end_col)


print("PART 1: ", part_1())
print("PART 2: ", part_2())

