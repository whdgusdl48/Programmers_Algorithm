"""
왕실의 나이트
"""

loc = str(input())

first = ['a','b','c','d','e','f','g','h']

loc2 = [first.index(loc[0]) + 1,int(loc[1])]

c = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

count = 0
for i in c:
    t = i
    nx = loc2[0] + t[0]
    ny = loc2[1] + t[1]
    if nx > 8 or nx < 1 or ny > 8 or ny < 1:
        continue
    count += 1

