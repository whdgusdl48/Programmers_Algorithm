"""
큰 수의 법칙
"""

n, m, k = map(int,input().split())
print(n, m, k)
data = list(map(int,input().split()))
print(data)

data.sort()
first = data[-1]
second = data[-2]
print(first,second)

answer = 0
count = 0
for i in range(m):
    if count == k:
        count = 0
        answer += second
    else:
        count += 1
        answer += first

"""
Greedy => 문제 변형
"""

# t는 수열 반복횟수
t = int(m / (k + 1)) * k + (m % (k + 1))
print(t * first + (m - t) * second)
