from collections import deque
n, m = map(int,input().split())
graph = []
tomato = []
all_count = 0
for i in range(m):
    temp = list(map(int,input().split()))
    graph.append(temp)
    for j in range(len(temp)):
        if graph[i][j] == 1:
            tomato.append((i,j))
        if graph[i][j] != -1:
            all_count += 1

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def bfs(x,y,tomato):
    q = deque(tomato)
    days = -1
    while q:
        days += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < m and ny >= 0 and ny < n:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = 1
                        q.append((nx,ny))

    for a in graph:
        if 0 in a:
            return -1
    return days
a = bfs(0,0,tomato)
print(a)
