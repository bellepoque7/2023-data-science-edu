'''
문제 포인트!
기존 bfs 와 달리 0을 만나면 추가적인 que append가 수행되어야함.
이를 위해 가장 최상단(바깥쪽) while문에 주난이가 점프할때마다 loop를 돌게
안쪽 while문에는 1을 만날때까지 퍼져가는 파동의 로직을 구현
if 그래프 == 1:
    그래프 ==0
    임시큐.append(좌표)
else:
    que.append(좌표)

안쪽 while 루프 수행 종료 후(파동이 모두 퍼져나갔다면)
임시큐를 원래 큐에 넣어 초기화(deepcopy 개념 생각)
'''
from collections import deque
import sys

read = sys.stdin.readline
global R, C, r1, c1, r2, c2, visited, a
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    global R, C, r1, c1, r2, c2, visited, a
    Que = deque([(r1, c1)])
    visited[r1][c1] = 1
    cnt = 0

    while True:
        cnt += 1    # 주난이가 한번 뛴다!!
        next_que = deque()  # 쓰러뜨린 친구들을 담을 큐

        while len(Que) > 0:
            r, c = Que.popleft()

            # 함수 종료 조건
            if r == r2 and c == c2:
                return cnt

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                # 지도 벗어나는지 범위 체크
                if nr < 0 + 1 or nr >= R + 1 or nc < 0 + 1 or nc >= C + 1:
                    continue
                # 방문 체크
                if visited[nr][nc] != 0:
                    continue

                # 다음 방문할 곳에 사람이 있는 경우
                if a[nr][nc] == '1':
                    next_que.append((nr, nc))   # 현재 큐에 담으면 step by step 이 안되므로 따로 임시큐에 저장
                else:
                    Que.append((nr, nc))     # 그외 현재 사용되는 큐에 담음

                visited[nr][nc] = 1     # 방문 체크

        Que = next_que


def main():
    global R, C, r1, c1, r2, c2, res, visited, a
    R, C = map(int, read().rstrip().split())
    visited = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
    a = [[0]]       # (1, 1) 시작을 맞추기 위함
    r1, c1, r2, c2 = map(int, read().rstrip().split())

    for _ in range(R):
        c = list(map(str, read().rstrip()))     # 맵에 #과 *이 있어서 문자형태로 받는 것이 편함
        a.append([0] + c)

    print(bfs())


if __name__ == '__main__':
    main()