# n = 10
# my_list = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
import sys
n = int(input())
my_list = list(map(int,sys.stdin.readline().split()))

S = [0]*(n)

S[0] = my_list[0]
for i in range(1,n):
    S[i] = max(S[i-1] + my_list[i],my_list[i])
print(max(S))