import sys
read = sys.stdin.readline


def main():
    N = int(read().rstrip())
    res = 0

    # N이 3보다 작아지면 의미가 없음
    while N >= 3:
        # 3의 배수 이면서 5의 배수가 아닌 경우에만 3키로 봉지에 담는다
        if N % 3 == 0 and N % 5 != 0:
           res += 1
           N -= 3
       # 나머지 경우 모두 5키로 봉지에 담음
        else:
            res += 1
            N -= 5

    if N != 0:
        print(-1)
    else:
        print(res)

if __name__ == "__main__":
    main()
