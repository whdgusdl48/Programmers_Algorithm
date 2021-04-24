n, m = map(int,input().split())

data = []
for i in range(n):
    data.append(list(map(int,input().split())))

print(data)

"""
def dfs(x,y):
    if x < 0 or x >= n or y < 0 and y >=  m:
        return False
    if data[x][y] == 0:
        data[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
           count += 1
print(count)
"""
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

from collections import deque
def bfs(x, y):
    # 현재 위치를 큐에 집어넣음
    q = deque()
    q.append((x,y))

    # 만약 현재 위치가 1이라면 아이스크림을 만들 수 없는 공간이거나 이미 탐색한 곳이므로 False 반환
    if data[x][y] == 1:
        return False

    # 현재 위치를 기준으로 BFS 탐색
    while q:
        x, y = q.popleft()
        # 현재 위치 값을 0에서 1로 변경
        data[x][y] = 1
        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 얼음 틀 범위에서 벗어나지 않으면서 그 위치의 값이 0인 경우에만 큐에 집어넣음
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
                q.append((nx,ny))
    # 하나의 아이스크림이 만들어지는 공간을 모두 탐색한 경우 True
    return True

cnt = 0

for i in range(n):
    for j in range(m):
        # 현재 위치에서 BFS 수행
        if bfs(i, j) == True:
            cnt += 1

print(cnt)