def stair(data):
    # 리스트의 길이를 n에 저장합니다.
    n = len(data)
    dp = [0 for i in range(n)]
    #dp는 밟은 점수의 합을 저장
    #1번계단만 있을때는 1번의 값이 정보
    dp[0] = data[0]
    #2번계단까지 있으면, 1,2번의 다 밟아야 이득
    dp[1] = data[0] + data[1]
    #3번 계단까지 있으면
    #1번밟고 3번계단 밟거나, 2번,3번 다 밟거나 중 최대값  
    dp[2] = max(data[0]+data[2], data[1]+data[2])

    #강사님 코드 -> 맨뒤에 dp[1] 틀림
    # dp[2] = max(dp[0] + data[2], dp[1])

    
    for i in range(3, n):
        # 두번째 안밟는 경우와 바로 전 안밟는 경우
        dp[i] = max(dp[i - 3] + data[i - 1], dp[i - 2]) + data[i]
    
    return dp[-1]


def main():
    data = [int(x) for x in input().split()]
    print(stair(data))


if __name__ == "__main__":
    main()