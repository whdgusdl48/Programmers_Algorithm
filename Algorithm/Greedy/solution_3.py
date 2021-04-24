"""
카드 게임
"""

n, m = map(int, input().split())

first_value = -1
for i in range(n):
    data = list(map(int, input().split()))
    if len(data) > m:
        print('배열의 길이를 넘어섰습니다')
        break
    a = min(data)
    first_value = max(a,first_value)
    print(first_value)