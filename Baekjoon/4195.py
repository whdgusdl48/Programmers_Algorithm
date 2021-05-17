import sys
input = sys.stdin.readline

test_case = int(input())

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,count,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a != b:
       parent[b] = a
       count[a] += count[b]

for _ in range(test_case):
    parent = {}
    count = {}

    m = int(input())

    for _ in range(m):
        a, b = map(str,input().split())
        # 중복없이 배열에 집어넣어야 한다.
        if a not in parent:
            parent[a] = a
            count[a] = 1
        if b not in parent:
            parent[b] = b
            count[b] = 1
        # 합치기
        union_parent(parent,count,a,b)
        print(count[find_parent(parent,a)])
