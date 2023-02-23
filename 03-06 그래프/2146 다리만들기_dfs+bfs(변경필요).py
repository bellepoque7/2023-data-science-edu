#목표 dfs로 각 섬을 숫자로 바꾸기 
import sys
from collections import *
#기본 재귀가 너무많이 들어가므로 리밋올리기
sys.setrecursionlimit(10**9)

#그래프 좌표 넣을 2d array
graph = []
#섬(1)의 좌표 넣을 리스트, 추후 큐 형태로 순환할 것
island = []
min_dist = 10e9
n = int(input())
visited = [[0]*n]*n

#섬 좌표 받기
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

# print(graph)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            island.append((i,j))
# print(island) #섬의 좌표 
# [(0, 0), (0, 1), (0, 2), (0, 7), (0, 8), (0, 9), (1, 0), (1, 1), (1, 2), (1, 3), (1, 8), (1, 9), (2, 0), (2, 2), (2, 3), (2, 8), (2, 9), (3, 2), (3, 3), (3, 4), (3, 9), (4, 3), (4, 9), (5, 9), (7, 4), (7, 5), (8, 4), (8, 5), (8, 6)] 

# 일단 모두 좌표를 돌면서 dfs로 재귀할거고... 
# 만약에 좌표가 0이면 멈추고 탈출할거고 그다음에 다른 좌표로 갈거임

dr = [-1,1,0,0] #상하좌우 
dc = [0,0,-1,1]

is_num = 2
def dfs(r,c,is_num):
    graph[r][c] = is_num
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < n and nc < n and nr >=0 and nc >=0:
            if graph[nr][nc] == 1 and visited[nr][nc] == 0:
                #섬 좌표있으면 어짜피 탐색할거니까 지워 
                if (nr,nc) in island:
                    island.remove((nr,nc))
                dfs(nr,nc,is_num)
                # print('end')
    #재귀 끝날때마다 그래프 확인하려면 하기 주석 제거 
    # for i in range(n):
        # print(graph[i])
    # print('----')
    return 

#그래프를 변형하되 섬마다 2,3,4 라고 표기하기
for i in island:
    dfs(i[0],i[1],is_num)
    is_num += 1

def bfs(n):
    global ans,min_dist
    check = [[-1] * n for _ in range(n)]
    q = deque(island)

    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            #다른 섬에 도착한 경우
            if graph[nr][nc] > 0 and graph[nr][nc] != n:
                min_dist = min(min_dist,check[r][c])
                return
            #바다이고, 방문한 적이 없다면
            if graph[nr][nc] == 0 and check[nr][nc] == -1:
                check[nr][nc] = check[r][c]+1
                q.append((nr,nc))

for i in range(2,is_num):
    bfs(i)
print(min_dist)
