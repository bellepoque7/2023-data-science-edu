import sys
n, m = map(int, sys.stdin.readline().split())
dot = list(map(int, sys.stdin.readline().split()))
dot.sort()

def dot_min(a):  # 선분 왼쪽의 중 가장 작음  점 구하기 
    if a < dot[0]:
        a = dot[0]
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2  #
        if dot[mid] < a:   
            start = mid + 1
        else:     #dot[mid] == a         # # mid = 2,0, dot[mid] = 10,1, a = 1
            end = mid - 1  # end  = 1, -1
    return end + 1 # end +1 = 0

def dot_max(b):   # 선분 오른쪽의  가장 큰 점 구하기

    if b >dot[-1]:
        b = dot[-1]
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2  # mid = 3,4
        if b < dot[mid]:  
            end = mid - 1
        else:         # b = 10, dot[mid] = 10
            start = mid + 1 
        # if dot[mid] < b:   
        #     start = mid + 1 # start = 3,4
        # else:     
        #     end = mid - 1
    return end + 1

my_list = []
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    my_list.append((dot_min(a),dot_max(b),  dot_max(b) - dot_min(a) + 1))
    # my_list.append(dot_max(b),dot_max(b) - dot_min(a) + 1)

for i in my_list:
    print(i)

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