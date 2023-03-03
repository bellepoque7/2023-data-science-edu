import sys
input =  sys.stdin.readline
global graph,visited,e,c
res = []
def dfs(s,num):  # 시작 s = 7, 끝 e = 3
	visited[s] = 1
	num+=1
	# print(num)

	if s == e:
		res.append(num)
		return
	print(graph[s])
    
	for i in graph[s]:
		if visited[i]!=0:
			continue
		dfs(i,num)

	# return res

# global graph,visited,e,c
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

s,e = map(int,input().split())
m = int(input())
# print(graph)   # [[], [], [], [], [], [], [], [], [], []]
# print(visited) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# print(s,e,m)  # 7,3,7

for _ in range(m):
    x,y = map(int,input().split())

    graph[x].append(y)
    graph[y].append(x)  # 이걸 넣어야할까? graph가 좀 지저분해지는거같은데.
# n 인덱스 부모에 자식값(value)
# print(graph) # [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]
c = []
print(dfs(s,0))
print(c)