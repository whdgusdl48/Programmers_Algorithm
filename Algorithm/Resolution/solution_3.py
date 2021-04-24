"""
게임 개발
"""
n, m = map(int,input().split())
print(n,m)

d = [[0] * m for _ in range(n)]
x, y, direction = map(int,input().split())
print(x,y,direction)
print(d)
d[x][y] = 1

maps = []
for i in range(m):
    data = list(map(int,input().split()))
    maps.append(data)
print(maps)

def left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

dx = [-1,0,1,0]
dy = [0,1,0,-1]

count = 1
turn_time = 0

while True:
    left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and maps[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if maps[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
