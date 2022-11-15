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