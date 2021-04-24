INF = 99999999

graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]

print(graph)

Adjust=[]

for i in range(len(graph)):
    temp = []
    for j in range(len(graph[0])):
        if i == j:
            continue
        else:
            if graph[i][j] != INF:
                temp.append((i,graph[i][j]))
            else:
                continue
    Adjust.append(temp)
print(Adjust)

graphs=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

def dfs(graph,v,visited):
    visited[v] = True
    print(v, end= '  ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

print(dfs(graphs,1,visited))
visited = [False] * 9

from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

print(bfs(graphs,1,visited))