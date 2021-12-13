with open('input.txt') as f:
    points, folds = [line.split('\n') for line in f.read().strip().split('\n\n')]
    points = [(int(x), int(y)) for x, y in [p.split(',') for p in points]]
    folds = [(f[11], int(f[13:])) for f in folds]

def part_1():
    visible = set()
    fold_dir, fold_line = folds[0]
    for x, y in points:
        if fold_dir == 'x' and x > fold_line: x = fold_line - (x - fold_line)
        elif fold_dir == 'y' and y > fold_line: y = fold_line - (y - fold_line)
        visible.add((x, y))
    return len(visible)

def part_2():
    visible = set(points)
    for fold_dir, fold_line in folds:
        visible_new = set()
        for x, y in visible:
            if fold_dir == 'x' and x > fold_line: x = fold_line - (x - fold_line)
            elif fold_dir == 'y' and y > fold_line: y = fold_line - (y - fold_line)
            visible_new.add((x, y))
        visible = visible_new
    code = [[' ']*10 for _ in range(40)]
    for x, y in visible: code[x][y] = '#'
    for row in code: print(''.join(row[::-1]))  # because mirror imaged
    return


print("PART 1: ", part_1())
print("PART 2: ", part_2())

