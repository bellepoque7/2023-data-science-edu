import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
read = sys.stdin.readline

global N, scv, visited

damage = [
    [9, 3, 1],
    [9, 1, 3],
    [3, 9, 1],
    [3, 1, 9],
    [1, 9, 3],
    [1, 3, 9]
]


def bfs():
    Q = deque()
    Q.append((scv[0], scv[1], scv[2]))
    # visited의 인덱스가 체력
    visited[scv[0]][scv[1]][scv[2]] = 1

    while len(Q) != 0:
        a, b, c = Q.popleft()  # a = 12, b = 10, c = 4

        if a == 0 and b == 0 and c == 0:
            break

        #6가지 데미지 입히는 방식이있으니까 모두 루프 돌아
        for i in range(6):
            
            #체력이 음수가 될 수 있으므로 max 함수 쓰기
            na = max(0, a - damage[i][0])
            nb = max(0, b - damage[i][1])
            nc = max(0, c - damage[i][2])

            #중복이면 해당 루프는 탈출
            if visited[na][nb][nc] != 0:
                continue

            Q.append((na, nb, nc))
            visited[na][nb][nc] = visited[a][b][c] + 1

    # 시작을 1에서 했기 때문에 1 빼줘야 됨
    return visited[0][0][0] - 1


def main():
    global N, scv, visited

    N = int(read().rstrip())
    scv = list(map(int, read().rstrip().split()))

    # 세마리 맞춰 놓는게 편함
    for i in range(3 - len(scv)):
        scv.append(0)
    # print(scv) # ex) 60  -> [60,0,0]

    # 최대 체력이 60이므로
    visited = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]

    print(bfs())


if __name__ == "__main__":
    main()
