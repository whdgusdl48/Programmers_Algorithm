n = int(input())
m = int(input())

adjust = [[] for _ in range(n + 1)]
# print(adjust)
for _ in range(m):
    a,b = map(int,input().split())
    adjust[a].append(b)
    adjust[b].append(a)

visited = [False] * (n + 1)

def dfs(visited,v,graph):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(visited,i,graph)

dfs(visited,1,adjust)

result = 0

for i in range(2,n+1):
    if visited[i] == True:
        result += 1

print(result)