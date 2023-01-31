import sys
read = sys.stdin.readline

def main():
    N = int(read().rstrip())
    a = []
    for i in range(N):
        x, y = map(int, read().rstrip().split())
        a.append((x, y))

    # print(a) #[(2,1),(8,3),(5,7)]
    
    # 시작시간 기준 정렬  최대로 우겨넣어서 통과하는게아닌. 그냥 전체종료시간만 구하면됨.
    a.sort()    #[(2,1),(5,7),(8,3)]
    # 첫 번째 소 도착 시간으로 세팅
    end = a[0][0]

    for cow in a:
        end = max(cow[0], end)  # 현재 시간이 도착 시간보다 늦으면 그대로 사용하고 빠르면 도착 시간으로 변경
        end += cow[1]   # 검문 시간 만큼 더하기

    print(end)


if __name__ == "__main__":
    main()
