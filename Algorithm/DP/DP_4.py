test_case = [
    [
        [1, 3, 3, 2],
        [2, 1, 4, 1],
        [0, 6, 4, 7]
    ],
    [
        [1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]
    ]
]
def solution(arr,n,m):
    d = [[0] * m for _ in range(n)]
    for i in range(len(arr)):
        d[i][0] = arr[i][0]
    # print(d)
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            if j == 0:
                d[j][i] = max(d[j][i-1],d[j+1][i-1]) + arr[j][i]
            elif j == len(arr)-1:
                d[j][i] = max(d[j][i - 1], d[j - 1][i - 1]) + arr[j][i]
            else:
                d[j][i] = max(d[j][i - 1],d[j + 1][i - 1], d[j - 1][i - 1]) + arr[j][i]
            # print(d[j][i])
    result = 0
    for i in range(n):
        result = max(result,d[i][m-1])
    return result
for i in range(len(test_case)):
    print(solution(test_case[i],len(test_case[i]),len(test_case[i][0])))
