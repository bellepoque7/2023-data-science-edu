#시간초과 O(n^2)

import sys
n  = int(input())
A = list(map(int,sys.stdin.readline().split()))
stack = [0]
# -1 로 초기화
ans = [-1 for i in range(len(A))] 


for i in range(1,len(A)):
    #어떤 조건과 수행
    j = i
    while True:
        if A[j] > A[stack[-1]]:
            ans[stack.pop()] = A[j]
            break
        else:
            # j를 업데이트
            j +=1
            # 끝까지 가도 없으면 탈출  -> 이거 끝가지 가는거 하지않고 할수있나? O(n^2)보다 낮아질수 있나?
            if j == n:
                break
    stack.append(i)
print(*ans)