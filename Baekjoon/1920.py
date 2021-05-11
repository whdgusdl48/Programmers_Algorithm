import sys
n = int(input())
A = list(map(int,sys.stdin.readline().split()))
m = int(input())
find_A = list(map(int,sys.stdin.readline().split()))

A.sort()

def binary_search(arr,target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        # print(mid)
        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        elif arr[mid] == target:
            return arr[start:end + 1].count(target)
    return 0
for i in find_A:
    print(binary_search(A,i))