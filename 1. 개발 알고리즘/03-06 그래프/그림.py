import sys
sys.setrecursionlimit(10 ** 6)
read = sys.stdin.readline

global R, C, a, visited, res, cnt
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    visited[r][c] = 1
    size = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= R or nc < 0 or nc >= C or visited[nr][nc] != 0 or a[nr][nc] == 0:
            continue

        size += dfs(nr, nc)

    return size


def main():
    global R, C, a, visited, res, cnt

    R, C = map(int, read().rstrip().split())
    a = []

    for i in range(R):
        temp = list(map(int, read().rstrip().split()))
        a.append(temp)

    cnt = 0
    res = 0

    visited = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if visited[i][j] == 0 and a[i][j] == 1:
                cnt += 1
                res = max(res, dfs(i, j))

    print(cnt)
    print(res)


if __name__ == "__main__":
    main()
