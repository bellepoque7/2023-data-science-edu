#이중루프 사용시 시간초과
#미리 누적합 리스트를 만들어놓고 
# 보고싶은 윈도우 크기 K 만큼 조회하는것은 누적합의 차로 도출 ㄴ

import sys
n, k = map(int,input().split())
my_list = list(map(int, sys.stdin.readline().split()))

p_sum = [0]

#이중 포문 수행할것을 O(n) 두번으로 수행 
for i in range(len(my_list)):
    p_sum.append(p_sum[i] + my_list[i])
res = -100000 

for i in range(k,len(my_list)+1):
    my_max = p_sum[i] - p_sum[i-k]
    res = max(my_max, res)
print(res)