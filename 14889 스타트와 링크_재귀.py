import sys
n = int(input())
graph = [] 
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))    # for i in range(n): print(graph[i])
start_team = []
link_team = [ i for i in range(n)]  #[0,1,2,3] 의미없는 값
ansArr=[] # ans min 으로 비교하면 지역변수에러

def cal(start_team, link_team):
    s_sum = 0
    l_sum = 0 
    for i in start_team: # start team = [0,1]
        for j in start_team:
            #i,j이 같은상황이면 그 값은 패스할것.
            if i == j:
                continue
            s_sum += graph[i][j]    #graph[0][1] 과 graph[1][0] 즉 1,2번 선수 능력치의 총합이 들어감. 
    for i in link_team:
        for j in link_team:
            if i == j:
                continue
            l_sum += graph[i][j]
    #모든 팀의 능력치비교를 ansArr에 저장
    ansArr.append(abs(s_sum - l_sum))

def dfs():
    #stat_team이 전체 명수의 절반을 채우면 break 조건
    if len(start_team) == n/2:
        #스타트 팀 아니면 나머지 링크팀으로 넣는다(set 집합 활용)
        cal(start_team, list(set(link_team)-set(start_team)))
        return

    for i in range(n):
        # stat팀에 아직 사람이 없거나.. 들어가려는 사람이  스타트팀보다 더 크다면 계속해서 진행
        if len(start_team) == 0 or i > max(start_team):
            start_team.append(i)
            dfs()
            start_team.pop()
dfs()
# print(ansArr)
print(min(ansArr))
