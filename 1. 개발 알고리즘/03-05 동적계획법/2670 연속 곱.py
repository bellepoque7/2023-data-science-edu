N = int(input())

arr =[]
for i in range(N):
    arr.append(float(input()))
# print(arr)
dp = [0 for i in range(len(arr))]

for i in range(len(dp)):
    if i == 0:
        dp[0] == arr[0]
    else:
        dp[i] = max(dp[i-1],1)*arr[i-1]
        # print(dp)
    
print('%0.3f' % max(dp))
# print(round(max(dp),3))

# print(1.1*1.2)