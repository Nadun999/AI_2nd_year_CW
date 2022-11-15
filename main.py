import random
# Maze = []

# # printing the maze array without brackets
# def printMaze(k):
#     for i in k:
#         for k in i:
#             print(k,end="   ")
#         print()
#     print("\n")

# # genarating the initial maze
# def initialMaze(width, height):
#     for i in range(0, height):
#         line = []
#         for j in range(0, width):
#             line.append('0')
#         Maze.append(line)
#
#
#     # choosing a random value point for the starting point as (b,a)
#     a = random.randint(0,5)
#     b = random.randint(0,1)
#
#     Maze[a][b] = 3
#
#     # chosing a random goal point as (x,y)
#     x = random.randint(0,5)
#     y = random.randint(4,5)
#
#     Maze[x][y] = 9
#
#     # creating 4 random barriers
#     for i in range(4):
#         barrier_x = random.randint(0,5)
#         barrier_y = random.randint(0,5)
#
#         if Maze[x][y] == Maze[barrier_x][barrier_y] or Maze[a][b] == Maze[barrier_x][barrier_y] or Maze[barrier_x][barrier_y] != '0':
#             continue
#         else:
#             Maze[barrier_x][barrier_y] = 1
#
#
#     # printing the newest maze
#     printMaze(Maze)


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


def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)

def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"
    return stack.pop()

stack = create_stack()

# creating an array to save the path
path = []

# initializing stating point
m = start_row
n = start_column
start = {m: n}
current = {m: n}

# adding starting point to the path
path.append(start)

push(stack, str(start))

first_search = maze[m][n-1]
second_search = maze[m-1][n]
third_search = maze[m+1][n]
fourth_search = maze[m][n+1]

a=1
# while (m == end_row) & (n == end_column):
while (a<10):
    if (first_search == 0) & (n!=0):
        m = m
        n = n - 1
        current = {m: n}
        path.append(current)
        a+=1
    elif (second_search == 0) & (m!=0):
        m = m - 1
        n = n
        current = {m: n}
        path.append(current)
        a+=1
    elif (third_search == 0) & (m!=5):
        m = m + 1
        n = n
        current = {m: n}
        path.append(current)
        a+=1
    elif (fourth_search == 0) & (n!=5):
        m = m
        n = n + 1
        current = {m: n}
        path.append(current)
        a+=1


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





# calling the initialMaze method
# initialMaze(6,6)




