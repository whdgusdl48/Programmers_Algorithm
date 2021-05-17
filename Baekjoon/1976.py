import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())
graph = []

for i in range(n):
    b = list(map(int,input().split()))
    graph.append(b)

t = list(map(int,input().split()))

parent = [i for i in range(n + 1)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(parent,i+1,j+1)

answer = set([parent[i] for i in t])
if len(answer) == 1:
    print('YES')
else:
    print('NO')