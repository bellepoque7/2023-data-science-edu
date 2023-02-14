import sys
from collections import deque
input = sys.stdin.readline

res = []
def bfs():
    q = deque()
    q.append([home[0], home[1]])
    while q:
        r, c = q.popleft()
        if abs(r - fest[0]) + abs(c - fest[1]) <= 1000:
            res.append('happy')
            return
        for i in range(n):
            #무한루프 방지
            if not visited[i]:
                nr, nc = conv[i]
                if abs(r - nr) + abs(c - nc) <= 1000:
                    q.append([nr, nc])
                    visited[i] = 1
    res.append("sad")
    return

t = int(input())
for i in range(t):
    n = int(input())
    home = [int(x) for x in input().split()]
    conv = []
    for j in range(n):
        x, y = map(int, input().split())
        conv.append([x, y])
    fest = [int(x) for x in input().split()]
    visited = [0 for i in range(n+1)] #home 제외
    bfs()
    
for i in res:
    print(i)