from collections import deque
import sys
readl = sys.stdin.readline


# N : 노드, M 간선, K: 최단거리, X 출발지
N,M,K,X = map(int,readl().split())
road = [list(map(int,readl().split())) for _ in range(M)]

visit = [0]*(N+1)
scnt = 1
tree = [[] for _ in range(N+1)]
q = deque()

ans = []

for a,b in road:
    tree[a].append(b)

for i in range(len(tree[X])):
    q.append((tree[X][i],scnt))

# print(q)

visit[X] = 0 

while q:
    a,cnt = q.popleft() # (2,1) (3,1)

    if visit[a] == 1: 
      continue
    visit[a] = 1
    
    if cnt == K:
        ans.append(a)    
    print(q,visit, a, cnt)
    if sum(visit) == N: 
        
        break # 다 방문했으면 종료!

    if len(tree[a]) == 0 : 
      continue
    ncnt = cnt+1
   
    for i in range(len(tree[a])):
        q.append((tree[a][i],ncnt))


if len(ans) == 0:
    print(-1)

else:
    ans.sort()
    for i in range(len(ans)):
        print(ans[i])
        