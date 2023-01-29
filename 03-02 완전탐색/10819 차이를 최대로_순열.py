#순열로 푸는법.
from itertools import permutations

n = int(input())
arr = list(map(int ,input().split()))

#모든 순열을 다 리스트에 넣는다. 
permu = list(permutations(arr, n))
# print(permu)
def calculator(li):
  total = 0
  for i in range(len(li)-1):
    total += abs(li[i]-li[i+1])
  return total

answer = -1e9
for li in permu:
  answer = max(answer, calculator(li))
print(answer)