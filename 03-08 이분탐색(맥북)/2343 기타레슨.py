#https://jainn.tistory.com/m/232

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

video = list(map(int, input().split()))

#vm에 강의 길이값의 최대를 넣음
vm = max(video)
#시작 위치 초기화
start = vm
#종료위치는 모든 강의를 1개 블루레이에 넣는 경우
end = sum(video)

#결과값 초기화
res = 10**9

#이진탐색 시작
while(start <= end):
    mid = (start+end)//2
    #최소 1개의 블루레이는 필요함
    cnt = 1
    #블루레이의 길이
    tmp = 0
    for i in range(n):
        if(tmp+video[i] <= mid):
            # 만약 현재 블루레이에 비디오를 더 넣을 수 있다면
            tmp += video[i]
        else:
            cnt += 1
            tmp = video[i]
        if(cnt > m):
            break
    if(cnt > m):
        start = mid+1
    else:
        end = mid-1
        if(mid >= vm):
            res = min(res, mid)

print(res)