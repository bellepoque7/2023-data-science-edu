import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

# print(paper)  # 2D array 
result = []

def solution(r, c, N) :
  #x,y = 0,0의 value에 대해서 color에 할당
  color = paper[r][c]
  # 원점부터 끝까지 탐색.
  for i in range(r, r+N) :
    #열도 탐색
    for j in range(c, c+N) :
      if color != paper[i][j] :
        solution(r, c, N//2)
        solution(r, c+N//2, N//2)
        solution(r+N//2, c, N//2)
        solution(r+N//2, c+N//2, N//2)
        return
  if color == 0 :
    result.append(0)
  else :
    result.append(1)


solution(0,0,N)
print(result.count(0))
print(result.count(1))