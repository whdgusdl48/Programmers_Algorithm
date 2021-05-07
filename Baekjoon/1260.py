n, m, start = map(int,input().split())

adjust = [[] for _ in range(n + 1)]
# print(adjust)
for _ in range(m):
    a,b = map(int,input().split())
    adjust[a].append(b)
    adjust[b].append(a)
    adjust[a].sort()
    adjust[b].sort()
visited = [False] * (n + 1)

def dfs(visited,v,graph):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == False:
            dfs(visited,i,graph)

dfs(visited,start,adjust)

print()
visited = [False] * (n + 1)

from collections import deque
def bfs(visited,v,graph):
    q = deque([v])
    visited[v] = True
    while q:
        st = q.popleft()
        print(st, end= ' ')
        for i in graph[st]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

bfs(visited,start,adjust)