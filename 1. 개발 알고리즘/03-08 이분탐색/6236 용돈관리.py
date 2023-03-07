#https://yeoooo.github.io/algorithm/BOJ6236/
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
budget = [int(input()) for _ in range(N)]
l,r = min(budget), sum(budget)
while l <= r:
    m = (l+r)//2
    now = m
    draw = 1

    #모든 예산에 루프돌리기
    for i in budget:
        #돈이 부족하면 초기화하고 인출 +1
        if now < i:
            now = m
            draw+=1
        #매일 값 지불
        now -= i
    # 인출횟수가 정해진 M보다 크면, 우측 절반 탐색(인출금액 상향)
    # m<max(budget)은 왜?
    if draw > M or m < max(budget):
        l = m+1
    # 인출횟수가 더 작으면, 좌측 절반탐색(인출금액 하향)
    else:
        r = m-1
        k = m
print(k)