#핵심은 남길애들을 prefix sum 구한다. 그리고 조합을 구하여서 남길애들이 많으면 스위칭횟수가 작으므로
#이 경향성ㅇ으로 찾을 수 있다.
from itertools import *

N,M = map(int,input().split())
lst = list(map(int,input().split()))

pdlst = [0]*(M+1)
for l in lst:
    pdlst[l] += 1

pmlst = list(permutations(range(1,M+1),M))


mn = int(1e9)
for pm in pmlst:
    cnt = 0
    i=0
    for prod in pm:
        for _ in range(pdlst[prod]):
            if lst[i] != prod:
                cnt+=1
            i+=1
    mn = min(mn,cnt)
                
print(mn)