import sys
from collections import deque
Q = deque()
m,n = map(int, sys.stdin.readline().split())
graph = []
visited = [[0]*m]*n
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            Q.append((i,j)) # deque([(3,5)])

# print(Q)
# print(graph)
# [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]
# bfs이죠

dr = [-1,1,0,0]
dc = [0,0,-1,1]
cnt = 0

def bfs():
    global cnt
    
    #큐에 자료값이 있다면
    while cnt !=2:
        
        #현재 Q 에 들어있는 좌표 수만큼 수행
        for i  in range(len(Q)):
            r,c = Q.popleft()
            visited[r][c] = 1
            # print(r,c)
            # break
            print(visited)
            break
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < n and nc < m and nr >=0 and nc >=0 and graph[nr][nc] == 0:
                    # print(nr,nc)
                    visited[nr][nc] = visited[r][c] + 1
                    Q.append((nr,nc))
                    
                # print(visited)
            cnt += 1
        # print(Q)
        print(cnt)
        break
bfs()
# for i in range(n):
#     print(visited[i])
print(cnt)