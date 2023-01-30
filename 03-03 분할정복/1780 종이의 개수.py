import sys
read = sys.stdin.readline

global N, a, res
def paper(r, c, size):
    global N, a, res
    # 탈출 조건
    if size == 1:
        # 종이 카운팅
        res[a[r][c] + 1] += 1
        return
        
    for i in range(r, r + size):
        for j in range(c, c + size):
            if a[i][j] != a[r][c]:
                # 세로 삼등분
                for i in range(3):
                    # 가로 삼등분
                    for j in range(3):
                        paper(r + (size // 3 * i), c + (size // 3 * j), size // 3)
                return
    # 모두 같은 색이었을 경우 처리
    res[a[r][c] + 1] += 1

def main():
    global N, a, res
    N = int(read().rstrip())
    a = [[]]
    for i in range(N):
        temp = list(map(int, read().rstrip().split()))
        a.append([0] + temp)
    res = [0 for i in range(3)]
    paper(1, 1, N)
    for i in res:
        print(i)


if __name__ == '__main__':
    main()