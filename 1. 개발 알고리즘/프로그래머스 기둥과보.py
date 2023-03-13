#https://school.programmers.co.kr/learn/courses/30/lessons/60061
# 하단 코드는 정답
'''
possible 함수는 하나라도 틀린게 있으면 False를 뱉어야하는 함수.
따라서 기저결과를 True로 설정하고, 이후 하나라도 틀린 구조(기둥,보)가나오면 False 로 표기하도록 해야함.
'''

import sys
input = sys.stdin.readline

def possible(answer):
	# can = False
	# x는 열좌표, y는 행좌표, a는 0이 기둥, 1이 보, b=1 설치, b=0 삭제
	for x, y, a in answer:
		if a ==0: # 기둥일때, x=2,y=2,a=p00
			# 바닥에 서있을때, 기둥위일때, 보에 한쪽 끝부분일떄 x2
			if y == 0 or [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer:
				# can = True
				# return can
				continue
			return False
		elif a ==1: #보일때
			if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
				# can = True
				# return can
				continue
			return False
	return True

def solution(n, build_frame):
	answer = []
	for frame in build_frame:
		x,y,a,b = frame
        #b==0 구조물 삭제
		if b == 0:
			answer.remove([x,y,a])
			if not possible(answer):
				answer.append([x,y,a])
        #b==1 구조물 설치
		elif b ==1:
			answer.append([x,y,a])
			if not possible(answer):
				answer.remove([x,y,a])
		print(sorted(answer))
	
	return sorted(answer)

def main():
	build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
	n = 5
	print(solution(n, build_frame))

if __name__ == '__main__':
	main()