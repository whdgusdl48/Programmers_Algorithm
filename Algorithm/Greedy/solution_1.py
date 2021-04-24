"""
1. 거스름돈
"""
money = int(input())

coin = [500,100,50,10]
count = 0
for i in coin:
    count += int(money / i)
    money = money % i

print(count)

