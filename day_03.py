import re

def parse_line(line):
    id_rex = r'#([0-9]+) '
    id = re.findall(id_rex, line)[0]
    id = int(id)

    pos_rex = r'@ ([0-9]+),([0-9]+): '
    pos = re.findall(pos_rex, line)[0]
    pos = tuple([int(p) for p in pos])

    size_rex = r': ([0-9]+)x([0-9]+)'
    size = re.findall(size_rex, line)[0]
    size = tuple([int(s) for s in size])

    return id, pos, size

def insert_rect(rect, fabric):
    y_begin = rect[1][0]
    x_begin = rect[1][1]
    y_width = rect[2][0]
    x_width = rect[2][1]

    for i in range(x_begin, x_begin + x_width):
        for j in range(y_begin, y_begin + y_width):
            fabric[i][j] += 1


with open("day_03.txt") as f:
    data = f.readlines()

    fabric = [[0 for _ in range(1001)] for _ in range(1001)]


for line in data:
    rect = parse_line(line)
    insert_rect(rect, fabric)

overlapping = 0
for line in fabric:
    for el in line:
        if el > 1:
            overlapping += 1
print(overlapping)
