import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a > b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int,input().split())

parent = [i for i in range(n)]
check = True
loc = 0
for i in range(m):
    a, b = map(int,input().split())
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
    else:
        loc = i+1
        check = False
        break

if check:
    print(0)
else:
    print(loc)
