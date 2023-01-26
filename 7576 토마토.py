from collections import deque
import copy 

def solve():
    #값 정의하기, 토마토 위치 받기 
    m, n = map(int,input().split())
    my_list = []
    for i in range(n):
        my_list.append(list(map(int,input().split())))
    que = deque()
    my_data = [[0]*m for _ in range(n)]

    #que와 my_data(토마토 숙성진행도) 셋팅
    #my_list에 1(토마토있는부분)만 복사해서 my_data 초기화 
    for i in range(m):
        for j in range(n):
            if my_list[j][i] == 1:
                # my_data[j][i] = 1
                que.append((j,i))


    dr = [-1,1,0,0] # 행:상하좌우
    dc = [0,0,-1,1] # 열:상하좌우

    result = -1 #일단 실패라고 선언

    # 탐색시작
    while que:
        result += 1
        quLen = len(que)
        for k in range(quLen):
            r, c = que.popleft()

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < n and nc < m and nr >=0 and nc >=0 and my_list[nr][nc] == 0:
                    my_data[nr][nc] = 1
                    que.append((nr,nc))
        print(que)
        break

    for i in range(m):
        for j in range(n):
            if my_data[j][i] == 0:
                return -1
    return result

print(solve())

