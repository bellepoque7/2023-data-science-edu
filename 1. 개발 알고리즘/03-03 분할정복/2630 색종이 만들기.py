import sys
read = sys.stdin.readline

global N, a, blue, white

def paper(r, c, size):
    global N, a, blue, white
    # 탈출 조건
    if size == 1:
        # 종이 카운팅
        if a[r][c] == 1:
            blue += 1
        else:
            white += 1
        return

    for i in range(r, r + size):
        for j in range(c, c + size):
            if a[i][j] != a[r][c]:
                paper(r, c, size//2)
                paper(r, c+ (size // 2), size//2)
                paper(r+(size // 2), c, size//2)
                paper(r+(size // 2), c+ (size // 2),size//2)
                return
    # 모두 같은 색이었을 경우 처리
    if a[r][c] == 1:
        blue += 1
    else:
        white += 1

def main():
    global N, a, blue, white
    N = int(read().rstrip())
    a = [[]]

    for i in range(N):
        temp = list(map(int, read().rstrip().split()))
        a.append([0] + temp)

    blue = 0
    white = 0
    paper(1, 1, N)
    print(white)
    print(blue)

if __name__ == '__main__':
    main()