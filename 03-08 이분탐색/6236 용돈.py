n, m = map(int, input().split())
daily = list(int(input()) for _ in range(n))
lt = min(daily)
rt = sum(daily)

# 이분탐색 시작
while lt <= rt:
    mid = (lt + rt) // 2		# 중간값. 인출할 금액
    charge = mid			# 현재 가진 돈. 처음 인출.
    num = 1				# 인출 횟수
    for i in range(n):			# n일 살기 시작
        if charge < daily[i]:		# 가진 돈이 부족하면 돈 인출
            charge = mid
            num += 1
        charge -= daily[i]		# 그날 다 살음

# m번보다 더 많이 인출하거나 인출한 금액이 하루를 다 살기에 적은 경우 (인출 금액이 적음)
    if num > m or mid < max(daily):	
        lt = mid + 1
    else:				# 인출 횟수가 m번보다 적거나 같음 (인출 금액이 많음)
        rt = mid - 1
        k = mid				# k값 저장

print(k)