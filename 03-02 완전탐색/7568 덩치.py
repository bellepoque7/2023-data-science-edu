<<<<<<< HEAD
#그냥 o(n^2) 때리기 

n = int(input())
 
data = [] # 입력받은 정보를 저장할 리스트 data
ans = [] # 등수정보를 저장할 리스트 ans
for i in range(n):
    a, b = map(int, input().split())
    data.append((a, b)) # 몸무계와 키를 묶어서 append 해줌
 
for i in range(n):
    count = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]: # 몸무게와 키 모두 자신보다 큰 사람의 수를 센다
            count += 1 
    ans.append(count + 1) # 덩치 등수는 자신보다 몸무계 키 모두 큰 사람의 수 + 1 이므로 count + 1을 ans에 append한다.
 
for d in ans:
    print(d,end=" ")
=======
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
>>>>>>> 363a7414a868f5273eb888715af9da62ae8902eb
