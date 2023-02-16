from heapq import *
import sys

n = int(sys.stdin.readline())
my_command = []
min_heap = []

for i in range(n):
    my_command.append(int(sys.stdin.readline()))
# print(my_command)

for i in range(len(my_command)):
    if my_command[i] ==0:
        if min_heap == []:
            print(0)
        else:
            print(heappop(min_heap))
    else:
        heappush(min_heap,my_command[i])