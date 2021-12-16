from functools import reduce

with open('input.txt') as f:
    line = list(f.read().strip())
    packets = ''.join([bin(int(x, 16))[2:].zfill(4) for x in line])

def bin2dec(chars):
    return int(chars, 2)

def parse_vers(pkt):
    pkt_version, pkt_id = bin2dec(pkt[:3]), bin2dec(pkt[3:6])
    if pkt_id == 4: 
        next_sub = 6
        while True:
            next_sub += 5
            if pkt[next_sub - 5] == '0': return pkt_version, next_sub
    else:
        if pkt[6] == '0':
            p, end = 22, bin2dec(pkt[7:22]) + 22
            while p < end:
                sub_version, inc = parse_vers(pkt[p:])
                pkt_version += sub_version
                p += inc
        else:
            end, num_subpkts = 18, bin2dec(pkt[7:18])
            for _ in range(num_subpkts):
                sub_version, inc = parse_vers(pkt[end:])
                pkt_version += sub_version
                end += inc
        return pkt_version, end

def parse(pkt):
    pkt_id = bin2dec(pkt[3:6])
    if pkt_id == 4: 
        next_sub = 6
        value = ''
        while True:
            next_sub += 5
            value += pkt[next_sub-4:next_sub]
            if pkt[next_sub - 5] == '0': return bin2dec(value), next_sub
    else:
        subpkts = []
        if pkt[6] == '0':
            p, end = 22, bin2dec(pkt[7:22]) + 22
            while p < end:
                sub_value, inc = parse(pkt[p:])
                subpkts.append(sub_value)
                p += inc
        else:
            end, num_subpkts = 18, bin2dec(pkt[7:18])
            for _ in range(num_subpkts):
                sub_value, inc = parse(pkt[end:])
                subpkts.append(sub_value)
                end += inc
        if pkt_id == 0: return sum(subpkts), end
        elif pkt_id == 1: 
            prod = 1
            for v in subpkts: prod *= v
            return prod, end
        elif pkt_id == 2: return min(subpkts), end
        elif pkt_id == 3: return max(subpkts), end
        elif pkt_id == 5: return 1 if subpkts[0] > subpkts[1] else 0, end
        elif pkt_id == 6: return 1 if subpkts[0] < subpkts[1] else 0, end
        elif pkt_id == 7: return 1 if subpkts[0] == subpkts[1] else 0, end


def part_1():
    return parse_vers(packets)[0]

def part_2():
    return parse(packets)[0]


print("PART 1: ", part_1())
print("PART 2: ", part_2())

