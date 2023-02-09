from itertools import *
# # n이 주어지면 n번째 감소하는 수를 출력
# # 1~9,10,20,21,30,31,32

n =  int(input())
my_list  = []
# 세자리 숫자면
for j in range(1,11):
    for i in combinations(range(0,10),j):
        comb = list(i)
        print(comb)
        comb.sort(reverse=True)
        my_list.append(''.join(map(str,comb)))
        my_list = list(map(int,my_list))
        # print(comb)
my_list.sort()
print(my_list)
if n >= 1023:
    print(-1)
else:
    print(my_list[n])