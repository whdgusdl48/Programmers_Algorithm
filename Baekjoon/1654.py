n, m = map(int,input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

def binary_search(arr,target):
    start = 1
    end = max(arr)
    answer = 0
    while start <= end:
        mid = (start + end) //2
        sum = 0
        for i in arr:
            if i >= mid:
                sum += i // mid
        if sum >= target:
            answer = mid
            start = mid + 1
        elif sum < target:
            end = mid - 1
    return answer

print(binary_search(arr,m))