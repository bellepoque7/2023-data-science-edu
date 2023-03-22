'''
check winner, add_score 함수 분리는 잘하였음.
다만 team1,team2 에  일관성없는 데이터가 들어가고 있음.
Ex
3
1 01:10
2 21:10
2 31:30

team1 = [1:00, 21:00, 48:00]
team2 = [21:00,31:30, 48:00]

21:00은 비기는 상황이라 둘 다 넣었는데 굳이 이렇게 수행할 필요가 없음. 또한 반례가 존재
4
1 10:00
2 20:00
2 25:00
1 30:00


개선방법) for문안의 add score에 따라 즉시 각 자 팀이 이기는 시간을 저장하는 설계 필요
ex
팀  시각   점수비교       액션
1  1:10  cnt1 >cnt2   해당시간 저장(start)
2  21:10 cnt1 = cnt2  해당 시간 종료(End) End-start 를 이기고있는 팀(1) 시간에 추가
2  31:00 cnt2 > cnt1  해당 시간 저장(start)
   48:00              해당 시간 종료(End) End-start 를 이기고있는 팀(1) 시간에 추가
'''

import sys
input = sys.stdin.readline

global cnt1,cnt2,time1,time2,win1,win2

def check_winner(cnt1,cnt2):
	global time1,time2,win1,win2
	if cnt1 == cnt2:
		win1 = False
		win2 = False
	elif cnt1 > cnt2:
		win1 = True
		win2 = False
	else: # cnt1 < cnt2
		win1 = False
		win2 = True
	
	if win1 and not win2:
		return 1
	elif win2 and not win1:
		return 2
	else:
		return 3
def add_score(team,now):
	global cnt1,cnt2,time1,time2,win1,win2

	if team == 1:
		 .append(now)
	elif team==2:
		time2.append(now)
	else:
		time1.append(now)  #예시2번,  now: 21:00 
		time2.append(now)

def now2time(timelist):
	# print('tt',timelist)
	if not timelist:
		return '00:00'
	ans = timelist[-1] - timelist[0]
	mm ='0000'
	ss ='0000'
	m = ans//60
	# print(m)
	s = ans % 60
	# print(s)
	mm = mm + str(m)
	ss = ss + str(s)
	# print('mm',mm)
	# print('ss',ss)

	return mm[-2:]+':'+ss[-2:]
	

def main():
	global cnt1,cnt2,time1,time2,win1,win2
	N = int(input())
	cnt1 = 0
	cnt2 = 0
	time1 = []
	time2 = []
	win1 = False
	win2 = False
	
	for i in range(N):
		team, time = input().split()
		time = time.split(':')
		now = int(time[0]) *60 + int(time[1])

		if team == '1':
			cnt1 += 1
		else:
			cnt2 += 1

		winteam = check_winner(cnt1,cnt2)  # 각 팀이이이고 있으면 1,2 무승부이면 3
		# print('nowwin',i, winteam)
		
		add_score(winteam,now)


	# print(time1,time2)
	# print(win1)
	# print(win2)
	if win1:
		time1.append(60*48)
		# 한번도 팀2가 이긴적이없으면, 슬라이싱 하지 않음.
		if len(time2) != 0:
			# print(1, time2) 
			time1 = time1[1:] 
	else:
		time2.append(60*48)
		if len(time1) != 0:
			time2 = time2[1:]
	# print('------')
	# print('time1,2이 이기고 있는 시간:')
	# for i in time1:
	# 	print(i//60,':',i%60, end = ' ')
	# 	print('')
	# 	pass

	# for i in time2:
	# 	print(i//60,':',i%60, end = ' ')
	# 	print('')
	# print('------')
	'''
    time1: [70, 1270]
    time2: [1890, 2880]
    '''

	print(now2time(time1))
	print(now2time(time2))

if __name__ == '__main__':
	main()