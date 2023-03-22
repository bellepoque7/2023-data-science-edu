## dfs함수(실제로는 bfs)로 좌표를 가지고 들어가자마자 vis 체크하면 시간 초과 x
from collections import deque
from itertools import *
import sys
sys.setrecursionlimit(10**6)
read=sys.stdin.readline
global res
n,m,k=map(int,read().split())
li=[[1 for i in range(m)] for j in range(n)]
for i in range(k):
    a,b,c,d=map(int,read().split())
    for j in range(b,d):
        for k in range(a,c):
            li[j][k]=0

vis=[[0 for i in range(m)] for j in range(n)]
# print(li)
def dfs(x,y):
    global res
    res=0
    vis[x][y] = 1
    q=deque()
    q.append((x,y))
    dr=[0,0,1,-1]
    dc=[1,-1,0,0]
    while len(q)>0:
        
        
        r=q[0][0]
        c=q[0][1]
        q.popleft()
        # if vis[r][c]==0:
            # vis[r][c]=1
        res=res+1
        # vis[r][c]=1
        # res=res+1

        print(r,c,'--------')
        for i in range(n-1,-1,-1):
            print(vis[i])
        
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if nr<0 or nc<0 or nr>n-1 or nc>m-1 or vis[nr][nc]==1 or li[nr][nc]==0:
                continue
            if (nr,nr) in q:
                continue
            else:
                q.append((nr,nc))
                vis[nr][nc]=1
            print(q)

ress=[]
for i in range(n):
    for j in range(m):
        if li[i][j]==1 and vis[i][j]==0:
            dfs(i,j)
            ress.append(res)
print(len(ress))
ress.sort()
for i in ress:
    print(i,end=' ')