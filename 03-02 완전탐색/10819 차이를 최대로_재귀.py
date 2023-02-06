import sys
n = int(input())
in_list = list(map(int ,sys.stdin.readline().split()))
visited = [False]*n
ansArr = []

def sol(my_list):
    #모든 값이 my_list에 들어왔으면
  if len(my_list) == n:
    total = 0
    # 리스트의 모든 값 계산하기
    for i in range(n-1):
      total += abs(my_list[i]- my_list[i+1])
    #계산 값 저장하기
    ansArr.append(total)
    return
    #재귀 시작
  for i in range(n):
    if not visited[i]:
      visited[i] = True
      my_list.append(in_list[i])
      sol(my_list)
      visited[i] = False
      my_list.pop()

sol([])
print(max(ansArr))


## 수정