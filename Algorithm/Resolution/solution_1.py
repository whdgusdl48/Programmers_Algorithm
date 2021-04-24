"""
상하좌우
"""

n = int(input())

move = list(map(str,input().split()))
print(move)

start_index = [1,1]
place = ['L','R','U','D']
x = [0,0,-1,1]
y = [-1,1,0,0]
for i in range(len(move)):
    moving = move[i]
    a = place.index(moving)
    if start_index[0] + x[a] > n or start_index[0] + x[a] < 1:
        continue
    if start_index[1] + y[a] > n or start_index[1] + y[a] < 1:
        continue
    start_index[0] += x[a]
    start_index[1] += y[a]


print(start_index)
