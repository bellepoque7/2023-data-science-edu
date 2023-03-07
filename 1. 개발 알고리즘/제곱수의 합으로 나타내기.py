from itertools import * 
import math
import numpy as np 
import time

np.random.seed(1)
n_list = np.random.randint(1,101,10)
print(n_list)
# n = int(input())
# n = 50 
def make_sq(n):
    start = time.time()
    n_sqrt = int(math.sqrt(n)) +1

    my_list = []
    for i in combinations(range(1,n_sqrt),2):
        if i[0]**2 + i[1]**2 == n:
            my_list.append(i)
        
    for i in range(1,n_sqrt):
        if (i**2)*2 == n:
            my_list.append(i)

    # print(my_list)
    end = time.time()
    print(end-start, print(n, my_list))

for i in n_list:
    make_sq(i)
