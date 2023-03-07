import sys

m,n,k = map(int,sys.stdin.readline().split())
visited = [[0 for _ in range(m)] for _ in range(n) ]
graph = [[0 for _ in range(m)] for _ in range(n) ]

for i in range(k):
    c, r = map(int,sys.stdin.readline().split())
    graph[r][c] = 1

# 좌표 찍어보기
# for i in range(n):
#     print(graph[i])

dr = [-1,1,0,0] #상하좌우
dc = [0,0,-1,1]
cnt = 0 
def dfs(r,c):
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >=0 and nc >=0 and nr < n and nc < m and visited[nr][nc] == 0 and graph[nr][nc] == 1:
            print(nr,nc)
            dfs(nr,nc)
            # return
    # return


for i in range(m):
    for j in range(n):
        if graph[j][i] == 1 and visited[j][i] == 0:
            cnt += 1
            dfs(j,i)
        # #중간결과를 보자
            for i in range(n):
                print(visited[i], j,i,'좌표에서 DFS')
            print('---------')
print(cnt)