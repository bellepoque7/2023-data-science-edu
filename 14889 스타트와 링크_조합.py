import sys
from itertools import *

read = sys.stdin.readline

global N, stat, visited
# 최솟값 문제
res = 1e9


def calc():
    start = []
    link = []

    # 계산 편하게 하기 위해 팀원들 list로 나눔
    for i in range(1, N + 1):
        # visited 표시 된 애들은 start 팀 아니면 link 팀
        if visited[i]:
            start.append(i)
        else:
            link.append(i)

    start_stat = 0
    link_stat = 0

    # 능력치 계산
    for i in range(N // 2):
        for j in range(N // 2):
            start_stat += stat[start[i]][start[j]]
            link_stat += stat[link[i]][link[j]]

    return abs(start_stat - link_stat)


def main():
    global N, stat, visited, res
    N = int(read().rstrip())
    stat = [[]]  # 인덱스 1번부터 사용하기 위해 행 하나 껴넣음
    for i in range(N):
        # 인덱스 0번부터 사용하기 위해 0 하나 껴넣음
        temp = [0] + list(map(int, read().rstrip().split()))
        stat.append(temp)
    # itertools 사용해서 조합 구현
    comb = list(combinations(range(1, N + 1), N // 2))

    for i in comb:
        # visited 다시 원복 시키기 어려워서 계속 새로 선언
        visited = [False for i in range(N + 1)]
        for j in i:
            # 조합에 선택된 애들 표시
            visited[j] = True
        res = min(calc(), res)

    print(res)


if __name__ == "__main__":
    main()