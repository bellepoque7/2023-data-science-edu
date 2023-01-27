'''
5
55 185
58 183
88 186
60 175
46 155
'''
import sys
n = int(sys.stdin.readline())
my_list = []
for i in range(n):
    my_list.append(tuple(map(int,sys.stdin.readline().split())))
# print(n)
# print(my_list)

my_rank_list = []
my_rank = 1
for i,j in enumerate(my_list):
    for k,l in enumerate(my_list):
    # print(j,my_list[i])
        if j[0] == my_list[k][0] and j[1] == my_list[k][1]:
            continue
        elif j[0] < my_list[k][0] and j[1] < my_list[k][1]:
            my_rank += 1
    # print(my_rank)
    my_rank_list.append(my_rank)
    my_rank = 1
print(*my_rank_list)



# 이중루프만들지말고 딕셔너리로 구현할까? 그럼 시간복잡도 n 일텐데
