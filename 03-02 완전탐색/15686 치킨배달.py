import sys
from itertools import combinations
read = sys.stdin.readline
'''
아이디어는 기존 치킨집갯수에서 뺴고 남을 치킨집 갯수의 조합을 모두 탐색해보는 것이다. 
만약 4개의 치킨집이 있고, 3개의 치킨집을 남긴다면
모든 경우의수 4개에 대해서 완전 탐색을 진행하는 것이다.
'''
global N, M, visited, a, house, chicken
res = 1e9
cnt = 0

def calc():
    global N, M, res, visited, a, cnt, house, chicken
    # 도시의 치킨거리. 모든 치킨 거리의 합
    city_dis = 0
    #각 하우스의 위치 튜플을 house_r, house_c 에 저장
    for house_r, house_c in house:
        # now_dis: 집 마다 제일 가까운 치킨집과의 거리 ->  즉 최솟값 저장 해야 됨
        now_dis = 1e9
        #치킨집 위치에 대하여 루프
        for i in range(len(chicken)):
            if visited[i]:  # 버린 치킨집은 무시
                continue
            chicken_r, chicken_c = chicken[i]
            # 현재까지 치킨거리 최솟값 갱신
            now_dis = min(now_dis, abs(house_r - chicken_r) + abs(house_c - chicken_c))
        city_dis += now_dis     # 현재 집 기준으로 가장 가까운 치킨거리 저장

    res = min(res, city_dis)

def main():
    global N, M, res, visited, a, cnt, house, chicken

    N, M = map(int, read().rstrip().split())
    a = []  #지도, 빈칸(0)   2d array
    house = [] #집 리스트(1)  튜플로 저장
    chicken = [] #치킨 리스트(2)  튜플로 저장

    for i in range(N):
        temp = list(map(int, read().rstrip().split()))
        a.append(temp)
        for j in range(len(temp)):
            # 집 위치 저장
            if a[i][j] == 1:
                house.append((i, j))
            # 치킨집 위치 저장
            elif a[i][j] == 2:
                chicken.append((i, j))
                cnt += 1

    # 치킨집 인덱스를 가지고 조합 돌림. 개수는 버릴 치킨집 개수. 즉 총 치킨집 - 남길 치킨집
    # 치킨집(cnt) 갯수가 4이고, 남길 갯수(M)이면, [1,2,3,4]의 4C3 [1],[2],[3],[4]
    for comb in combinations(range(cnt), cnt - M):
        visited = [False for i in range(cnt)]   # 치킨집 수 만큼 [F,F,F,F]
        # 버린 치킨집 체크
        for i in comb: # [1]
            visited[i] = True

        calc()

    print(res)


if __name__ == "__main__":
    main()
