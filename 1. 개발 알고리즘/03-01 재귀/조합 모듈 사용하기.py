import itertools
import sys

a,b = map(int,input().split())
my_list = [i for i in range(1,a+1)]
# print(my_list)
for i in itertools.combinations(my_list, b):
    print(*i)