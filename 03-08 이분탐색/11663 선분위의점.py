import sys

n, m = map(int, sys.stdin.readline().split())
dot = list(map(int, sys.stdin.readline().split()))
dot.sort()


def dot_min(a):  # 선분 중 가장 작은 점 구하기 
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if dot[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1


def dot_max(b):   # 선분 중 가장 큰 점 구하기
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if b < dot[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(dot_max(b) - dot_min(a) + 1)

# import sys
# n,m = map(int,sys.stdin.readline().split())
# dots = tuple(map(int,sys.stdin.readline().split()))
# lines = []
# for i in range(m):
#     lines.append(tuple(map(int,sys.stdin.readline().split())))
# print(n,m)
# print(dots)
# print(lines)

#완전탐색 O(n^2) 시간초과
# for i in lines:
#     cnt = 0
#     for j in dots:
#         if j >= i[0] and j <= i[1]:
#             cnt +=1 
#     print(cnt)