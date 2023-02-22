#수강생 코드
#test12번에 대해서 TLE. heappush(customer,[price,t-1]) 이 시간이 완전 탐색처럼
#시간이 소요됨에따른 에러. 힙구조를 활용하는 것은 좋으나 코드 개선이 필요함
import sys
import heapq

readl = sys.stdin.readline
N = int(input())
customers = []
for _ in range(N):
	P, T = map(int,readl().split())
	customers.append([-P, T])

customers = sorted(customers, key=lambda x: (x[0], x[1]))
heapq.heapify(customers)
confirm = [0 for _ in range(10001)]
print(customers)

while customers:
	price, t = heapq.heappop(customers)
	if t >= 1:
		#만약 price가 현재 최대값이니까(시간에관계없이)
		#confirm 리스트에 넣는 과정을 반복수행한다.
		if confirm[t] == 0:
			confirm[t] = price
		else:
			if t >= 2:
				#또는 t를 찾아가는 법을 동적으로 설계한다.
				# confirm 리스트의 값중에 비어 있는 중 마지막 인덱스를 t로 저장한다.
				heapq.heappush(customers, [price, t-1])
print(-sum(confirm))