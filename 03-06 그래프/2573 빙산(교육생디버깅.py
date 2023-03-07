import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

global graph, R, C, visited
dr = [-1, 1, 0, 0] #상, 하, 좌, 우
dc = [0, 0, -1, 1]


# def melt(r, c):
# 	visited[r][c] = 1
# 	ans = 0

# 	for i in range(4):
# 		nr = r + dr[i]
# 		nc = c + dc[i]

# 		# 주변이 그래프에서 벗어났거나, 방문한곳이 아니면
# 		if nr < 0 or nr >= R or nc < 0 or nc >= C or visited[nr][nc] != 0:
# 			continue
# 		if graph[nr][nc] != 0: # 주변 4방향이 빙산이면 패스 
# 			continue

# 		if graph[nr][nc] == 0:
# 			ans += 1

# 	return ans

def melt(r,c):
    ans = 0 
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr <0 or nr >= R or nc < 0 or nc >= C:
            continue
        if graph[nr][nc] == 0:
            ans += 1
    return ans
    # pass


def dfs(r, c):
	visited[r][c] = 1

	for i in range(4):
		nr = r + dr[i]
		nc = c + dc[i]

		if nr < 0 or nr >= R or nc < 0 or nc >= C or visited[nr][nc] != 0:
			continue
		if graph[nr][nc] == 0:
			continue
		dfs(nr, nc)


def main():
	global graph, R, C, visited
	R, C = map(int, input().split())
	graph = []
	mx = 0
	for i in range(R):
		x = list(map(int, input().split()))
		mx = max(mx, max(x))
		graph.append(x)
	year = 0

	cnt = 0
	div = True
	while True:

		if year > mx:
			div = False
			break

		visited = [[0 for _ in range(C)] for _ in range(R)]  #C,R 변경
		cnt = 0
		for i in range(R):
			for j in range(C):
				if graph[i][j] != 0 and visited[i][j] == 0:
					dfs(i, j)
					cnt += 1
		#CNT 잘찍히는지 확인

		# for i in range(R):
		# 	print(graph[i])
		# print('-------')
		# print(cnt)

		if cnt >=2:
			break

		visited = [[0 for _ in range(C)] for _ in range(R)] #C,R 변경

		for i in range(R):
			for j in range(C):
				if graph[i][j] != 0 and visited[i][j] == 0:
					graph[i][j] = max(0,graph[i][j] -melt(i, j)) 
                    #여기가 문제. 실시간으로 melt 업데이트하면 graph가 변형됨
                    #따라서 melt는 graph2에 녹아야하는 2d-array를 생성하고
                    #graph = graph - graph2 형식으로 업데이트해야함
                    '''
                    0 0 0 0             0 0 0 0
                    0 1 7 0  -> 옳게된 예 0 0 4 0
                    0 0 0 0             0 0 0 0
                    '''
					

		year += 1

	if div: # 빙산이 2개로 쪼개져서 탈출한 경우
		print(year)
	else:  # 위경우에 해당하지 않으면 
		print(0)


if __name__ == '__main__':
	main()