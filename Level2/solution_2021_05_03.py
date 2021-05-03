def correct_str(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def string_check(str):
    count = 0
    for i in str:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True
        
def solution(p):
    answer = ''
    if len(p) == 0:
        return ''
    index = correct_str(p)
    u = p[:index + 1]
    v = p[index + 1:]
    if string_check(u) == True:
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
    return answer
