def solution(n):
    answer = 0
    if n < 3:
        return n
    before1 = 1
    before2 = 2
    
    for i in range(3,n+1):
        answer = before1 + before2
        before1 = before2
        before2 = answer
    return answer % 1234567
