n,m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

print(graph)

# def dfs(graph,x,y,prev):
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return -1
#     if graph[x][y] == 0:
#         return -1
#     if x == n and y == m:
#         return graph[x][y]
#     else:
#         graph[x][y] += prev
#         dfs(graph,x + 1,y,graph[x][y])
#         dfs(graph,x,y+1,graph[x][y])
#
# dfs(graph,0,0,0)
# print(graph[n-1][m-1])


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

from collections import deque
def bfs(graph,x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(graph,0,0))
