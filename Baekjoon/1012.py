import sys
sys.setrecursionlimit(10000)

test_case = int(input())
arr = []
for i in range(test_case):

    n, m, k = map(int,input().split())
    graph = [[0] * m for _ in range(n)]
    check = [[False] * m for _ in range(n)]
    for i in range(k):
        x,y = map(int,input().split())
        graph[x][y] = 1

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
# print(graph)
    def dfs(x,y,cnt):
        check[x][y] = True
        graph[x][y] = cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if graph[nx][ny] == 1 and check[nx][ny] == False:
                    check[nx][ny] = True
                    graph[nx][ny] = cnt
                    dfs(nx,ny,cnt)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and check[i][j]== False:
                cnt += 1
                dfs(i, j,cnt)

    arr.append(cnt)

for i in arr:
    print(i)
