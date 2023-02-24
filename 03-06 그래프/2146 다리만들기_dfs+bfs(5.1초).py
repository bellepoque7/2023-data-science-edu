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
visited = [[0 for _ in range(n)] for _ in range(n)]

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
                # if (nr,nc) in island:
                    # island.remove((nr,nc))
                dfs(nr,nc,is_num)

#그래프를 변형하되 섬마다 2,3,4 라고 표기하기
for i in island:
    if graph[i[0]][i[1]] == 1:
        dfs(i[0],i[1],is_num)
        is_num += 1


#visited 초기화

# 숫자표기된 graph 보기
# for i in range(n):
        # print(graph[i])

def bfs(island_num):
    global ans,min_dist
    visited2 = [[0 for _ in range(n)] for _ in range(n)]
    q = deque(island)
    # print(q)
    for i in range(n):
        for j in range(n):
            if graph[i][j] == island_num:
                visited2[i][j] = 1
    
    # for i in range(n):
        # print(visited2[i])

    # print(len(q))
    while q:
        r,c = q.popleft()
        # 현재 탐색하려는 좌표가. bfs하려는 섬(n)이거나 바다(0)이면 진행하기
        if (graph[r][c] == island_num) or(graph[r][c] == 0 ):
            for i in range(4):
                nr = r+dr[i]
                nc = c+dc[i]
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue
                # print('check loop',r,c,nr,nc)
                #바다이고, 방문한 적이 없다면
                if graph[nr][nc] == 0 and visited2[nr][nc] == 0:
                    visited2[nr][nc] = visited2[r][c]+1
                    q.append((nr,nc))
                    # print('append')
                #다른 섬에 도착한 경우
                if graph[nr][nc] > 0 and graph[nr][nc] != island_num:
                    min_dist = min(min_dist,visited2[r][c])
                    # print('check')
                    return
                
        # for i in range(n):
            # print(visited2[i])
        # print('----')

for i in range(2,is_num):
    #i 번째 섬을 확장해나가기
    bfs(i)
    # break
print(min_dist-1)
