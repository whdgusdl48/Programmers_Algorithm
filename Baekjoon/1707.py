import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

test_case = int(input())
answer = []
for i in range(test_case):

    v, e = map(int,input().split())

    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)

    for i in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)


    def dfs(start, color):
        visited[start] = color
        for i in graph[start]:
            if visited[i] == 0:
                if not dfs(i, -color):
                    return False
            elif visited[start] == visited[i]:
                return False
        return True
    ans = True
    for i in range(1,v+1):
        if visited[i] == 0:
            ans = dfs(i,1)
            if not ans:
                break
    if ans:
        answer.append('YES')
    else:
        answer.append('NO')

for i in answer:
    print(i)