import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n + 1)
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def get_smallest_node():
    # 현재 거리중에 가장 거리가 작은 노드를 찾는 함수
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def algorithm(start):
    distance[start] = 0
    # 초기 인덱스는 거리가 0이므로 초기화
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    print(distance)
    for i in range(n-1):
        now = get_smallest_node()
        print('now : ',now)
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
        print(distance)
algorithm(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print('infinity')
    else:
        print(distance[i])
