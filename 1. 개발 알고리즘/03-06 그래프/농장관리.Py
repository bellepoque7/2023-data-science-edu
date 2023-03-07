import sys
sys.setrecursionlimit(10 ** 6)
read = sys.stdin.readline

global R, C, a, visited, res, flag
dr = [-1, 1, 0, 0, -1, -1, 1, 1]    # 8방향
dc = [0, 0, -1, 1, -1, 1, -1, 1]


def dfs(r, c):
    global R, C, a, visited, res, flag
    visited[r][c] = 1

    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]

        # 범위 체크
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            continue
        '''
        다음번이 더 높으면 산봉우리 안됨. nr, nc 방문 여부 상관 없이 높으면 안되므로 방문보다 먼저 체크. 
        안되더라도 같은 숫자 그룹은 끝까지 방문하면서 방문처리 해야 다음에 안들어옴
        '''
        if a[nr][nc] > a[r][c]:
            flag = False

        # 방문 체크
        if visited[nr][nc] != 0:
            continue

        # 값 다르면 무시. 같은 값인 그룹만 확인해야 됨
        if a[nr][nc] != a[r][c]:
            continue

        dfs(nr, nc)


def main():
    global R, C, a, visited, res, flag

    R, C = map(int, read().rstrip().split())
    a = []

    for i in range(R):
        temp = list(map(int, read().rstrip().split()))
        a.append(temp)

    visited = [[0 for _ in range(C)] for _ in range(R)]

    res = 0

    for i in range(R):
        for j in range(C):
            if visited[i][j] == 1:
                continue

            flag = True
            dfs(i, j)
            if flag:
                res += 1

    print(res)


if __name__ == "__main__":
    main()
