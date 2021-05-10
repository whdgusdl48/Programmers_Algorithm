test_case = int(input())

from collections import deque
answer = []
for i in range(test_case):
    l = int(input())
    start_index = list(map(int,input().split()))
    target_index = list(map(int,input().split()))

    dp = [[0] * (l) for _ in range(l)]
    visited = [[False] * (l) for _ in range(l)]
    dx = [1,1,2,2,-1,-1,-2,-2]
    dy = [2,-2,1,-1,2,-2,1,-1]
    def bfs(x,y):
        q = deque([(x,y)])
        visited[x][y] = True
        while q:
            t_x, t_y = q.popleft()
            if visited[t_x][t_y] == True and t_x == target_index[0] and t_y == target_index[1]:
                return dp[t_x][t_y]

            for i in range(len(dx)):
                nx = t_x + dx[i]
                ny = t_y + dy[i]
                # print(nx,ny)
                if 0 <= nx < l and 0<= ny <l and visited[nx][ny] != True:
                    dp[nx][ny] = dp[t_x][t_y] + 1
                    visited[nx][ny] = True
                    q.append((nx,ny))

    bfs(start_index[0],start_index[1])
    answer.append(dp[target_index[0]][target_index[1]])

for i in range(len(answer)):
    print(answer[i])
