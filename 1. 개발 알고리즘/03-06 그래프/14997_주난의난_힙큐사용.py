'''
진행하는 cnt를 저장.
1에 도착하면 cnt+1
0에 도착하면 cnt 그대로

cost 맵을 만들어서 해당 위치에 도착하는 최소 비용저장.
또한 최소비용 먼저 탐색을 위한 heap 구조 설정
'''

import sys
from collections import deque
from heapq import heappop, heappush
readl = sys.stdin.readline

N,M = map(int,readl().split())
y1,x1,y2,x2= map(int,readl().split())
mapp = [list(readl().strip()) for _ in range(N)]
cost = [[(int(1e9)) for _ in range(M)] for _ in range(N)]
    
def bfs():
    d=[(0,1),(0,-1),(1,0),(-1,0)]
    hp=[]
    heappush(hp,(0,y1-1,x1-1))
    cost[y1-1][x1-1] = 0

    while hp:
        cnt,r,c = heappop(hp)
        if cost[r][c] < cnt : continue
        
        for dr,dc in d:
            nr = r+dr
            nc = c+dc

            if not 0<=nr<N : continue
            if not 0<=nc<M : continue
            if cost[nr][nc] <= cnt+1 : continue
            
            if mapp[nr][nc] == '#':
                return cost[r][c]+1 

            if mapp[nr][nc] == '0':
                ncnt=cnt
            
            elif mapp[nr][nc] == '1':
                ncnt = cnt+1
                
            heappush(hp,(ncnt,nr,nc))
            cost[nr][nc] = min(cost[nr][nc],ncnt)
        
print(bfs())