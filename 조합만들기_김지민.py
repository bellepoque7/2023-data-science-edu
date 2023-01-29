# n, m = map(int, input().split())
n = 3
m = 2
arr = [x for x in range(1, n+1)] # 1.2.3
res = []
tmp = []

def dfs(nums, cnt, tmp): # (1) [1,2,3],[0],[], # (2) [2.3]. [1],[1] # (3) [3],[2],[1,2]
    # print('start', nums, cnt, tmp)
    # global res
    if cnt == m:
        print('check')
        res.append(tmp)
        # for i in tmp:
            # print(i, end =" ")
        # print()
        print(res)
    else:
        for i in range(len(nums)):
            # print(len(nums))
            tmp.append(nums[i]) 
            print('for_loop',i,nums[i+1:], cnt+1, tmp)
            dfs(nums[i+1:], cnt+1, tmp) #  (1) [2,3], [1], [1]  (2)  [3], [2], [1,2]
            print('for_loop2',res)
            tmp.pop()

dfs(arr, 0, tmp)
print(res)