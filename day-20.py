with open('input.txt') as f:
    algorithm, image = f.read().strip().replace('.', '0').replace('#', '1').split('\n\n')
    algorithm = dict(zip(list(range(len(algorithm))), list(algorithm)))
    image = [list('0' + x + '0') for x in image.split('\n')]
    image = [['0']*len(image[0])] + image + [['0']*len(image[0])] 

def enhance(image):
    bg = image[0][0]
    image = [[bg,bg] + row + [bg,bg] for row in image]
    image = [[bg]*len(image[0])] + [[bg]*len(image[0])] + image + [[bg]*len(image[0])] + [[bg]*len(image[0])]
    num_rows, num_cols = len(image), len(image[0])
    new_image = [['0']*num_cols for _ in range(num_rows)]
    for r in range(1, num_rows - 1):
        for c in range(1, num_cols - 1):
            neighbours = image[r-1][c-1:c+2] + image[r][c-1:c+2] + image[r+1][c-1:c+2]
            binary = int(''.join(neighbours), 2)
            new_image[r][c] = algorithm[binary]
    return [row[1:-1] for row in new_image[1:-1]]


def part_1():
    enhanced_img = enhance(enhance(image))
    return sum([row.count('1') for row in enhanced_img])

def part_2():
    enhanced_img = image
    for _ in range(50): enhanced_img = enhance(enhanced_img)
    return sum([row.count('1') for row in enhanced_img])


print("PART 1: ", part_1())
print("PART 2: ", part_2())

