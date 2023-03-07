import bisect

for _ in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    for a in A:
        cnt += (bisect.bisect(B, a-1))
    print(cnt)

'''
bisect.bisect(a, x, lo=0, hi=len(a), *, key=None)
- 정렬된 순서를 유지하도록 a에 x를 삽입할 위치를 찾습니다.
- bisect_left()와 비슷하지만, a에 있는 x의 기존 항목 뒤(오른쪽)에 오는 삽입 위치를 반환합니다.
'''
