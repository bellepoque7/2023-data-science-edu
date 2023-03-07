#문제
# 재귀에서 전달하는 파리미터이 r,c 값이 바뀌었었음 

import sys
read=sys.stdin.readline
n=int(read())
li=[]
for i in range(n):
  c=list(map(int,read().strip()))
  li.append(c)
# print(li)

def cal(r,c,x):
  cnt=0
  # if r == 0 and c == 4 and x ==2:
  #   print('check')
  for i in range(c,c+x):
    for j in range(r,r+x):
      if li[i][j]==1:
        cnt+=1
  if cnt == x*x:
    return '1'
  if cnt == 0:
    return '0'
        # pass
    # if r == 0 and c == 4 and x ==2:
    #   print('check2')
    
  cnt=0
  dc=[c,c,c+x//2,c+x//2] #왼위 오위 왼아 오아 
  dr=[r,r+x//2,r,r+x//2]
  
  res=''
  for i in range(4):
    res+=cal(dr[i],dc[i],x//2)
  return '(' + res +')'

print(cal(0,0,n))