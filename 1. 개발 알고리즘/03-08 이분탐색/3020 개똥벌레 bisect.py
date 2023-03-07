import sys
from bisect import *
read = sys.stdin.readline


def main():
    N, H = map(int, read().rstrip().split())
    down = []
    up = []
    for i in range(N):
        if i % 2 == 0:
            down.append(int(read().rstrip()))
        else:
            up.append(int(read().rstrip()))

    # 최솟값 구하는 문제
    res = int(1e9)
    cnt = 0
    down.sort()
    up.sort()
    # 높이 1부터 H까지 다 해보기
    for i in range(1, H + 1):
        # left는 값을 왼쪽으로 반환 하므로 반환값부터 끝까지 다 만나는 장애물임. 개수는 N // 2 - down_cnt
        down_cnt = bisect_left(down, i)
        # right는 값을 오른쪽으로 반환 하므로 H - i 를 탐색하면 같은 값 오른쪽을 반환해줌. 반환값부터 끝까지 다 만나는 장애물임. 개수는 N // 2 - up_cnt
        up_cnt = bisect_right(up, H - i)
        # 파괴 하는 장애물 개수
        sum = N - down_cnt - up_cnt

        # 최솟값 갱신 되는 경우
        if sum < res:
            res = sum
            cnt = 1

        # 최솟값과 같은 경우
        elif sum == res:
            cnt += 1

    print(res)
    print(cnt)


if __name__ == '__main__':
    main()