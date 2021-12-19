with open('input.txt') as f:
    groups = f.read().strip().split('\n\n')
    maps = {}
    for scanner, group in enumerate(groups):
        beacons = [tuple([int(y) for y in x.split(',')]) for x in group.split('\n')[1:]]
        maps[scanner] = beacons

# let scanner 0 be at (0,0,0)
SCANNERS = [(0,0,0)]
TRIANGLE_POINTS = {}

DIRECTIONS = [(0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,0,1), (2,1,0)]
NEGATIONS = [(1,1,1), (1,1,-1), (1,-1,1), (1,-1,-1), (-1,1,1), (-1,1,-1), (-1,-1,1), (-1,-1,-1)]

def rebase(base, coordinates):
    """ returns coordinates transformed relative to the base """
    return set([(p[0]-base[0], p[1]-base[1], p[2]-base[2]) for p in coordinates])

def transform(point, dirn, neg):
    return (point[dirn[0]]*neg[0], point[dirn[1]]*neg[1], point[dirn[2]]*neg[2])

def reorient(beacons):
    """ returns all possible orientations of the set of beacons """
    return [set([transform(coords, d, n) for coords in beacons]) for d, n in [get_transformer(i) for i in range(len(DIRECTIONS)*len(NEGATIONS))]]

def length_between(p1, p2):
    return sum([(p1[i]-p2[i])**2 for i in range(3)])

def get_triangles(beacons):
    # return all possible triangles (defined by ascending length of sides) formed from a given group of beacons
    num_beacons = len(beacons)
    triangles = set()
    for i in range(num_beacons):
        for j in range(i + 1, num_beacons):
            for k in range(j + 1, num_beacons):
                a, b, c = beacons[i], beacons[j], beacons[k]
                triangle = tuple(sorted([length_between(a,b), length_between(a,c), length_between(b,c)]))
                triangles.add(triangle)
                TRIANGLE_POINTS[triangle] = (a,b,c)
    return triangles

def get_transformer(n):
    return DIRECTIONS[n//len(NEGATIONS)], NEGATIONS[n%len(NEGATIONS)]

def translate(translator, point):
    return (translator[0] + point[0], translator[1] + point[1], translator[2] + point[2])

def new_beacons_translated(common_triangle, new_beacons, mapped_beacons):
    triangle_points = TRIANGLE_POINTS[common_triangle]
    base_point = triangle_points[0]
    reoriented_common_points = reorient(rebase(base_point, triangle_points))
    for beacon in mapped_beacons:
        rebased_beacons = rebase(beacon, mapped_beacons)
        for i, translation in enumerate(reoriented_common_points):
            if translation.issubset(rebased_beacons):
                dirn, neg = get_transformer(i)
                new_beacons = [transform(beacon, dirn, neg) for beacon in new_beacons]
                something = transform(base_point, dirn, neg)
                scanner = [beacon[n] - something[n] for n in range(3)]
                SCANNERS.append(scanner)
                return [translate(scanner, p) for p in new_beacons]

def part_1():
    mapped_beacons, mapped_triangles = set(maps[0]), get_triangles(maps[0])
    unmapped_scanners = set(maps.keys())
    unmapped_scanners.remove(0)
    while len(unmapped_scanners) > 0:
        for sc in unmapped_scanners:
            new_triangles = get_triangles(maps[sc])
            common_triangles = mapped_triangles.intersection(new_triangles)
            if len(common_triangles) >= 220:   # 220 = 12 choose 3
                beacons_to_add = new_beacons_translated(common_triangles.pop(), maps[sc], mapped_beacons)
                unmapped_scanners.remove(sc)
                mapped_triangles = mapped_triangles.union(new_triangles)
                mapped_beacons = mapped_beacons.union(beacons_to_add)
                break
    return len(mapped_beacons)

def part_2():
    ans = 0
    for sc1 in SCANNERS:
        for sc2 in SCANNERS:
            manhattan_distance = abs(sc1[0]-sc2[0]) + abs(sc1[1]-sc2[1]) + abs(sc1[2]-sc2[2])
            ans = max(manhattan_distance, ans)
    return ans


print("PART 1: ", part_1())
print("PART 2: ", part_2())

