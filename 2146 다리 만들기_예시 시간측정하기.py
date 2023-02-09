import sys
from itertools import *
import time

# n =  int(input())
# graph  = []
# for i in range(n): 
#     graph.append(list(map(int, sys.stdin.readline().split())))
start = time.time()
n = 10
graph = [[1, 1, 1, 0, 0, 0, 0, 2, 2, 2], [1, 1, 1, 1, 0, 0, 0, 0, 2, 2], [1, 0, 1, 1, 0, 0, 0, 0, 2, 2], [0, 0, 1, 1, 1, 0, 0, 0, 0, 2], [0, 0, 0, 1, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 3, 3, 0, 0, 0, 0], [0, 0, 0, 0, 3, 3, 3, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# for i in range(n):
#     print(graph[i])

corrd_comb = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            corrd_comb.append((i,j,graph[i][j]))

min_dist = 10e9
for i in combinations(corrd_comb,2):
    if i[0][2] != i[1][2]:
        min_dist = min(min_dist, abs(i[0][0]-i[1][0]) + abs(i[0][1]-i[1][1])-1)
print(min_dist)
end = time.time()
print(end - start)