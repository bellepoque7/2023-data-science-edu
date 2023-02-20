from itertools import * 
import math

# n = 50 
n = int(input())
n_sqrt = int(math.sqrt(n)) +1
visited = [0 for _ in range(n_sqrt)]
# 0~ 7까지의 visited 선언
# [0, 0, 0, 0, 0, 0, 0, 0]
# print(visited)
my_list = []
for i in combinations(range(1,n_sqrt),2):
    if i[0]**2 + i[1]**2 == n:
        my_list.append(i)
    
for i in range(1,n_sqrt):
    if (i**2)*2 == n:
        my_list.append(i)

# print(my_list)
print(len(my_list))
