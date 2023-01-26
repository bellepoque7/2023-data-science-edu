import sys
from heapq import * 
n = int(sys.stdin.readline())
my_list = []
for i in range(n):
    temp = int(sys.stdin.readline().strip())
    heappush(my_list,temp)

sum = 0
total_sum = 0 
for i in range(len(my_list)-1):
    a = heappop(my_list)
    b = heappop(my_list)
    sum = a+ b
    total_sum += sum 
    heappush(my_list,sum)
    # print(i,my_list,a,b)
print(total_sum)