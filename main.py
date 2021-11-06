graph = []
steps = []
cameras = []


def get_next(pos, offset_row, offset_col):
    new_pos = [pos[0] + offset_row, pos[1] + offset_col]

    if graph[new_pos[0]][new_pos[1]] == 'W':
        return None
    if graph[new_pos[0]][new_pos[1]] == 'U':
        return get_next(new_pos, -1, 0)
    if graph[new_pos[0]][new_pos[1]] == 'L':
        return get_next(new_pos, 0, -1)
    if graph[new_pos[0]][new_pos[1]] == 'D':
        return get_next(new_pos, 1, 0)
    if graph[new_pos[0]][new_pos[1]] == 'R':
        return get_next(new_pos, 0, 1)

    if steps[new_pos[0]][new_pos[1]] != -1:
        return None
    return new_pos


def pre_process_cameras():
    for coord in cameras:
        x = coord[0]
        y = coord[1]

        while graph[x][y] != "W":
            if graph[x][y] == 'S':
                return False
            if graph[x][y] == '.':
                steps[x][y] = -2
            x += 1

        x = coord[0]
        y = coord[1]
        while graph[x][y] != "W":
            if graph[x][y] == 'S':
                return False
            if graph[x][y] == '.':
                steps[x][y] = -2
            x -= 1

        x = coord[0]
        y = coord[1]
        while graph[x][y] != "W":
            if graph[x][y] == 'S':
                return False
            if graph[x][y] == '.':
                steps[x][y] = -2
            y += 1

        x = coord[0]
        y = coord[1]
        while graph[x][y] != "W":
            if graph[x][y] == 'S':
                return False
            if graph[x][y] == '.':
                steps[x][y] = -2
            y -= 1
    return True


rows, columns = map(int, input().split(" "))

start = None

for x in range(rows):
    line = input()
    graph.append(line)
    if "S" in line:
        y = line.find("S")
        start = [x, y]
    elif "C" in line:
        y = line.find("C")
        cameras.append([x, y])

for x in range(rows):
    row = []
    steps.append(row)
    for y in range(columns):
        row.append(-1)

if pre_process_cameras():
    steps[start[0]][start[1]] = 0
    current = [start]
    next_coord_list = []
    step = 0

    while current:
        step += 1
        for coord in current:
            next_coord = get_next(coord, -1, 0)  # going up.
            if next_coord:
                next_coord_list.append(next_coord)
                steps[next_coord[0]][next_coord[1]] = step

            next_coord = get_next(coord, 0, -1)  # going left.
            if next_coord:
                next_coord_list.append(next_coord)
                steps[next_coord[0]][next_coord[1]] = step

            next_coord = get_next(coord, 1, 0)  # going down.
            if next_coord:
                next_coord_list.append(next_coord)
                steps[next_coord[0]][next_coord[1]] = step

            next_coord = get_next(coord, 0, 1)  # going right.
            if next_coord:
                next_coord_list.append(next_coord)
                steps[next_coord[0]][next_coord[1]] = step

        current = next_coord_list
        next_coord_list = []

for x in range(rows):
    for y in range(columns):
        if graph[x][y] == '.':
            if steps[x][y] < 0:
                print(str(-1))
            else:
                print(steps[x][y])
