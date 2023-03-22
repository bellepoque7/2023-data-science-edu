import sys
input = sys.stdin.readline

def main():

	N = int(input())
	cnt1 = 0
	cnt2 = 0
	time1 = ['00','00']
	time2 = ['00','00']
	w_time1 = ['00','00']
	w_time2 = ['00','00']

	win1 = False
	win2 = False
	for i in range(N):
		team, time = input().split()
		mm,ss = time.split(':')
		# print('nowscore',cnt1,cnt2)
		if team == '1':
			cnt1 += 1
			if not win1:
				time1[0] = mm			
				time1[1] = ss
			else:
				w_time1[0] = mm			
				w_time1[1] = ss
			# print('time2',time1,w_time1)
		else:
			cnt2 +=1
			if not win2:
				time2[0] = mm			
				time2[1] = ss
			else:
				w_time2[0] = mm			
				w_time2[1] = ss
			# print('time2',time2,w_time2)

		if cnt1>cnt2:
			win1 = True
			win2 = False
		else:
			win1 = False
			win2 = True

		
		# print(win1)
		if cnt1 == cnt2:
			# print('score',cnt1,cnt2)
			if not win1:

				# print('nono',i)
				# print('nownext',int(mm), int(time1[0]),int(ss), int(time1[1]))
				new_mm = int(mm)- int(time1[0])
				# print(new_mm)
				new_ss = int(ss)- int(time1[1])
				# print('new_ss',new_ss)
				# print('nexttime0',time1)
				if new_ss <0:
					new_ss += 60
					new_mm -= 1
				else:	
					if new_ss > 0:
						# print('aaaa')
						time1[1] = str(new_ss)
					elif 0<= new_ss<10:
						time1[1] = '0'+str(new_ss)
						# print('a',new_ss)
						# print(time1[1])
					
					if new_mm>0:
						time1[0] = str(new_mm)
					
					elif 0<= new_mm<10:
						time1[0] = '0'+str(new_mm)
					# print(time1)
						
	
			elif not win2:
				
				# print('where')
				new_mm = int(time2[0]) - int(mm)
				new_ss = int(time2[1]) - int(ss)
				if new_ss <0:
					new_ss += 60
					new_mm -= 1
				else:	
					if new_ss > 0:
						# print('aaaa')
						time2[1] = str(new_ss)
					elif 0<= new_ss<10:
						time2[1] = '0'+str(new_ss)
						# print('a',new_ss)
						# print(time1[1])
					
					if new_mm>0:
						time2[0] = str(new_mm)
					
					elif 0<= new_mm<10:
						time2[0] = '0'+str(new_mm)
					
		
	if win1:
		new_mm = 48- int(w_time1[0]) 
		new_ss = 0- int(w_time1[1])
		if new_ss <0:
			new_ss += 60
			new_mm -= 1

		if new_mm<10:
			time1[0] = '0'+str(new_mm)
		if new_ss <10:
			time1[1] = '0'+str(new_ss)
			# print('ss',time1[1])
		else:	
			time1[0] = str(new_mm)
			time1[1] = str(new_ss)
		# print('new',time1)
	elif win2:
		# print('winner')
		new_mm = 48- int(w_time2[0])
		new_ss = 0- int(w_time2[1])
		if new_ss <0:
			new_ss += 60
			new_mm -= 1

		if new_mm<10:
			time2[0] = '0'+str(new_mm)
			# print('winnermm',time2[0])
		else:
			time2[0] = str(new_mm)
		if new_ss <10:
			time2[1] = '0'+str(new_ss)
		else:
			# print(new_mm)
			
			time2[1] = str(new_ss)
			# print('winnermmdddd',time2[0])
		
		
	wintime1 = ':'.join(time1)
	wintime2 = ':'.join(time2)
	print(wintime1)
	print(wintime2)
if __name__ == '__main__':
	main()