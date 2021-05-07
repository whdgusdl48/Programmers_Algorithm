from collections import deque
from collections import Counter
from functools import reduce

n = int(input())
graph = []
for _ in range(n):
    temp = list(map(int,input()))
    graph.append(temp)

group = [[0]*n for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
find = 2
from collections import deque

def bfs(x,y,find):
    q = deque([(x,y)])
    group[x][y] = find
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] == 1 and group[nx][ny] == 0:
                    graph[nx][ny] = find
                    group[nx][ny] = find
                    q.append((nx,ny))

cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and group[i][j] == 0:
            cnt += 1
            bfs(i, j, cnt)

print(cnt)

ans = reduce(lambda x,y : x+y, group)

ans = [x for x in ans if x > 0]

ans = sorted(list(Counter(ans).values()))
print('\n'.join(map(str,ans)))