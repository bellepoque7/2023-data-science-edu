import sys
read = sys.stdin.readline


def main():
    N = int(read().rstrip())
    #dp[i] 해당 날의 상담을 하면 받는 보상의 누적
    dp = [0 for _ in range(N + 4)]

    a = [0]

    for i in range(N):
        #t는 걸리는 시간, P는 보수임
        t, p = map(int, read().rstrip().split())
        a.append((t, p))

    # 뒤부터 첫날로 오는 방법. 이 문제는 이게 편함
    for i in range(N, 0, -1):
        t, p = a[i]
        # 상담 끝나는 날 = 시작날짜와 + 걸리는 시간
        end = i + t
        # print(i, dp)

        # 끝나는 날짜가 퇴사일 넘어가는 경우
        if end > N + 1:
            # 현재 상담 불가능. 다음날에 나온 최댓값이 현재까지 최댓값
            dp[i] = dp[i + 1]
        # 현재 일을 하면 다음날 작업을 못할수도 있기 때문에 다음날까지 최댓값이랑 비교 해야 됨
        # print(dp)
        else:
            dp[i] = max(dp[i + 1], dp[end] + p)
    
    # print(dp)
    print(dp[1])


if __name__ == '__main__':
    main()

