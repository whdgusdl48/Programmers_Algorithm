"""
1이 될때 까지
"""

target , n = map(int,input().split())

count = 0
while target != 1:
    if target % n == 0:
        print(target)
        count += 1
        target = target // n
    else:
        target -= 1
        count += 1

print(count)