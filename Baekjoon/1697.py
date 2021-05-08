start, target = map(int,input().split())
from collections import deque

visited = [False] * 100001
def bfs(start):
  count = 0
  q = deque([(start,count)])
  # visited[v] = True
  while q:
    v,count = q.popleft()
    if visited[v] == False:
      visited[v] = True
      if v == target:
        return count
      count += 1
      if v + 1 < 100001:
        q.append((v+1,count))
      if v - 1 >= 0:
        q.append((v-1,count))
      if v * 2 < 100001:
        q.append((v * 2,count))
  return count
print(bfs(start))
