import sys
read = sys.stdin.readline


def main():
    N = int(read().rstrip())
    a = [[]]

    for i in range(N):
        temp = list(map(int, read().rstrip().split()))
        a.append([0] + temp)

    dp = [[0 for _ in range(N + 4)] for _ in range(N + 4)]
    # print(dp) # n=5 일때 8*8에 대한 dp 테이블 생ㅇ성

    for i in range(1, N + 1):
        # i 번째 줄은 숫자가 i개
        for j in range(1, i + 1):
            # 윗줄을 비교 해야 됨. 둘중에 누굴 받을 것인가
            # 위에서 번저가는게 아니고 해당층에서, 그 위층까징의 sum 즉 dp테이블을 선택하는 형식
            #dp[i] i 줄에 있는 경로탐색된 합의 결과
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + a[i][j]
    print(dp)
    print(max(dp[N]))


if __name__ == "__main__":
    main()
