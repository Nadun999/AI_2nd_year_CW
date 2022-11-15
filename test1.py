import random

height = 6
width = 6

maze = []
for i in range(0, height):
    line = []
    for j in range(0, width):
        line.append(0)
    maze.append(line)

start_column = random.randint(0,1)
start_row = random.randint(0,5)

end_column = random.randint(4,5)
end_row = random.randint(0,5)

maze[start_row][start_column] = 5
maze[end_row][end_column] = 8

for k in range(4):
    barrier_column = random.randint(0,5)
    barrier_row = random.randint(0,5)
    maze[barrier_row][barrier_column] = 1

for i in maze:
    print(i, "\n")


def heuristic_cost():
    count_y = 0
    gy = end_row
    gx = end_column
    while (count_y < 6):
        count_x = 0
        while (count_x < 6):
            h_cost = max(abs(count_x - gx), abs(count_y - gy))
            print('heusristic cost for ' + str(count_y) + ',' + str(count_x) + ' are ' + str(h_cost))
            count_x += 1
        count_y += 1

heuristic_cost()