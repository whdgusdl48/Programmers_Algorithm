
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


for i in range(m):
    a, num1, num2 = map(int,input().split())
    if a == 0:
        union(parent,num1,num2)
    else:
        if find_parent(parent,num1) == find_parent(parent,num2):
            print('YES')
        else:
            print('NO')

