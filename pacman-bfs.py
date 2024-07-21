a = input().split(' ')
a = tuple(int(i) for i in a)
g = input().split(' ')
g = tuple(int(j) for j in g)
size = input().split(' ')
size = tuple(int(k) for k in size)
maze = []
for i in range(size[0]):
    r = list(input())
    maze.append(r)

explored = []
node = a
queue = [node]
parent = {a: None}

while queue:
    node = queue.pop(0)
    if node not in explored:
        explored.append(node)
    
    if node == g:
        break

    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    for direction in directions:
        next_node = (node[0] + direction[0], node[1] + direction[1])
        if 0 <= next_node[0] < size[0] and 0 <= next_node[1] < size[1]:
            if next_node not in explored and maze[next_node[0]][next_node[1]] != '%':
                queue.append(next_node)
                if next_node not in parent:
                    parent[next_node] = node

path = []
node = g
while node is not None:
    path.append(node)
    node = parent[node]
path.reverse()

print(str(len(explored)))
for i in explored:
    print(str(i[0]) + " " + str(i[1]))

print(str(len(path) - 1))
for j in path:
    print(str(j[0]) + " " + str(j[1]))
