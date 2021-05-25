import sys
input = sys.stdin.readline

n = int(input())

graph = []

for i in range(n):
    a = list(map(int, str(input().replace('\n',''))))
    graph.append(a)

answer = ''
def recursive(graph,start,end,n):
    color = graph[end][start]
    ch = False
    global answer
    for i in range(start, start + n):
        if ch:
            break
        for j in range(end, end + n):
            if graph[j][i] != color:
                answer += '('
                recursive(graph,start,end, n//2)
                recursive(graph,start + n//2 , end , n//2)
                recursive(graph,start, end + n//2 ,n//2)
                recursive(graph,start+n//2,end+n//2,n//2)
                answer += ')'
                ch = True
                break

    if not ch:
        if color == 1:
           answer += '1'
        else:
            answer += '0'
    print(answer)
recursive(graph,0,0,n)
print(answer)