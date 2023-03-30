
'''
dist array 를 만드는 코드를 모듈화해야한다.
현재 dist[i][i+1] 로 무조건 방향성있게 ex 1->2 , 2->3 3->4  진행하므로 결과모음을 보면 4등분이 되는걸 확인
이는 첫번째 물건이 주어지면 나머지가 자동적으로 정렬되어 원하는 순열방향으로 진행할 수 없었다. 
25%에서 정답이 막힌것이 그 이유
'''
from itertools import *
from collections import deque
import sys
input = sys.stdin.readline

global C,R,graph,sr,sc,er,ec,res

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(r0,c0,r1,c1):
	
	Q = deque()
	Q.append((r0,c0))
	visited = [[0 for _ in range(C)]for _ in range(R)]
	visited[r0][c0] = 1
	find = 0
	ans = 0
	while Q:
		r,c = Q.popleft()

		if r == r1 and c== c1:
			return visited[r][c]-1

		for i in range(4):
			nr = r + dr[i]
			nc = c + dc[i]

			if nr<0 or nr>=R or nc<0 or nc>=C:
				continue
			if visited[nr][nc] !=0:
				continue
			if graph[nr][nc]=='#':
				continue

			Q.append((nr,nc))
			visited[nr][nc] = visited[r][c] + 1
		

def main():
	global C,R,graph,sr,sc,er,ec,res
	C,R = map(int,input().split())

	graph=[]
	items=[]
	sr,sc =0,0
	er,ec = 0,0
	idx = 1
	#idx =0 : 출발지
	for i in range(R):
		graph.append(list(input().rstrip()))
		for j in range(C):
			
			if graph[i][j] == 'X':
				items.append((idx,i,j))
				idx+=1
			elif graph[i][j] == 'S':
				sr =i
				sc = j
				graph[i][j] ='.'

			elif graph[i][j]== 'E':
				er =i
				ec = j
	
	# for i in range(R):
	# 	print(graph[i])
	# print(items) # 물건들의 idx, 좌표 [(1, 1, 2), (2, 1, 5), (3, 3, 3), (4, 4, 4)]
	door = idx # 마지막 idx를 door 로 저장 
	# 
	dist =[[0 for _ in range(door+1)]for _ in range(door+1)]
	# for i in range(len(items)+2):
	# 	print(dist[i])
		
	dist[0][door] = bfs(sr,sc,er,ec)
	dist[door][0] = bfs(sr,sc,er,ec)
    
	for idx,r, c in items:
		d = bfs(sr,sc,r,c)
		dist[0][idx]= d
		dist[idx][0] = d

	for idx, r, c in items:
		d= bfs(r,c,er,ec)
		dist[idx][door] =d
		dist[door][idx] = d

	for item in combinations(items,2):
		(idx1,r1,c1) , (idx2,r2,c2) = item
		# print(idx1,idx2)
		d = bfs(r1,c1,r2,c2)
		dist[idx1][idx2] =  d
		dist[idx2][idx1] =  d
	# for i in range(door+1):
	# 	print(dist[i])
	'''
    [0, 1, 4, 4, 6, 8]
    [1, 0, 3, 3, 5, 7]
    [4, 3, 0, 6, 8, 10]
    [4, 3, 6, 0, 2, 4]
    [6, 5, 8, 2, 0, 2]
    [8, 7, 10, 4, 2, 0]    
    '''
    
	res = []
	kk =1e9

	for item in permutations(range(1,idx+1)):
		ans =0
		
		# print(item) #(1, 2, 3, 4)
        #기존 정답
        # way = [0] + list(item) + [door]
		# for i in range(door):
		# 	ans += dist[way[i]][way[i+1]]
		# res = min(res,ans)
		for i in range(door): #
			# print(i)
			if i == 0:
				ans += dist[0][item[i]] 
				continue
				# print(ans)
			elif i < door: # i=1,2,3,4
				ans += dist[item[i]][item[i+1]]
				# print(i,ans)
		res.append(ans)
		# break

		# ans += dist[i][door] # 이거 왜필요함?
		# res = min(ans,kk) # 주석처ㅓ리
	print(res)
    
	
		
if __name__ =='__main__':
	main()