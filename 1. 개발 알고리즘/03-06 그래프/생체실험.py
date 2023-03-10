import sys
from collections import deque
Q = deque()
m,n = map(int, sys.stdin.readline().split())
graph = []
visited = [[0 for _ in range(m)] for _ in range(n)] 

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            Q.append((i,j)) # deque([(3,5)])
            visited[i][j] = 1

# print(graph)
# [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]

dr = [-1,1,0,0]
dc = [0,0,-1,1]
day_cnt = 0

def bfs():
    global day_cnt
    #큐에 자료값이 있다면
    while Q:
        #현재 Q 에 들어있는 좌표 수만큼 수행
        for i  in range(len(Q)):
            r,c = Q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < n and nc < m and nr >=0 and nc >=0 and graph[nr][nc] == 0 and visited[nr][nc] == 0:
                    # print(nr,nc)
                    visited[nr][nc] = visited[r][c] + 1
                    Q.append((nr,nc))
                    
                # print(visited)
        day_cnt += 1

        # 잘모르면 시각화해서 봅시다.
        # print(Q)
        print(day_cnt,'일차 감염이 끝나면')
        for i in range(n):
            print(visited[i])
        print('---')
        

# 남은 생쥐가 있는지 없는지 체크
def check():
    for i in range(n):
        for j in range(m):
            # 방문하지도 않(못)했고, 살아있는 생쥐가 있다면
            if visited[i][j] == 0 and graph[i][j]==0:
                print(-1)
                return
    # 위에 분기가 안걸렸으면 정상 종료
    print(day_cnt-1)

bfs()
check()

        
#cnt_mouse: 23마리