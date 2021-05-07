from collections import deque
n, m = map(int,input().split())
graph = []
for _ in range(n):
    temp = list(map(int,input()))
    graph.append(temp)

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def bfs(x,y):
    q = deque([(x,y)])

    while q:
        x,y = q.popleft()
        min_val = 1e9
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if graph[nx][ny] != 0 and graph[nx][ny] == 1:
                    graph[nx][ny] = min(min_val,graph[x][y]) + 1
                    q.append((nx,ny))

bfs(0,0)
print(graph[n-1][m-1])