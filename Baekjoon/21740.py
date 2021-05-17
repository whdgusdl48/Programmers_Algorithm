import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
,j 
if 6 in arr:
    arr.insert(arr.index('6'),6)
else:
    arr.insert(arr.index(max(arr)),max(arr))

answer = ''
for i in arr:
    answer += str(i)
print(answer)
