from heapq import *
import sys
max_heap = []
n = int(input())
for i in range(n):
    input_num = int(sys.stdin.readline().strip())
    if input_num == 0:
        if max_heap != []:
            print(-heappop(max_heap))
        else:
            print(0)            
    else:
        heappush(max_heap, -input_num)
# print(max_heap)