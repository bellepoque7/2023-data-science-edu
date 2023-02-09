
import sys
n,m  = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))

#start와 end는 절단기의 높이(h)의 범위
#h높이와 집으로 가져가려하는 나무의길이(m)는 반비례함
#따라서 h = 0 부터 max(array)까지 이분탐색을 진행
start = 0
end = max(array)
ans = []
#통나무 길이 다합하기

# 0 에서 5 
while start <= end:
    mid = (start+end)//2
    # print(mid)
    #해당 값으로 통나무 샤샥 짜르고 그 길이 다더하기
    res = 0
    for i in array:
        if i > mid:
            # print(i-mid)
            res += (i-mid)
    ans.append((mid,res))
    #통나무 길이 합이 목표값과 같다면
    if res == m:
        # print('break?')
        break
    #통나무총 길이 합이 목표보다 크다면, 절단기 높이 올려야함
    if res > m:
        start = mid +1
    #통나모 총 길이의 합이 목표보다 작다면, 절단기 높이 내려야함
    else: #res < m:
        end = mid -1


ans.sort(key = lambda x : x[1])
# print(ans)
if ans[0][1] == m:
    print(ans[0][1])
else:
    print(ans[1][0])

