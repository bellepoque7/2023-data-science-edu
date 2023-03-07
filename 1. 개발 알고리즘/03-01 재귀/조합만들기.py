import sys
read = sys.stdin.readline
global N, M, visited

def comb(cnt, start):
    # 종료 조건. M개의 숫자를 골랐으면 출력
    if cnt == M:
        # 1부터 N까지 돌면서 선택한 숫자 출력
        for i in range(1, N + 1):
            if visited[i]:
                print(i, end=' ')
        print()
        return
    
    # start부터 N + 1까지 반복
    for i in range(start, N + 1):
        # 선택한 숫자 체크
        visited[i] = True
        # 선택한 채로 다음 단계로 이동. i이하는 볼 필요 없으므로 start를 i + 1로 보냄
        comb(cnt + 1, i + 1)
        # i가 선택된 경우를 돌렸으니 선택 해제
        visited[i] = False


def main():
    global N, M, visited
    N, M = map(int, read().rstrip().split())
    visited = [False for i in range(N + 1)]
    # 0개 골랐고 1부터 시작하므로 매개변수를 0, 1로 보냄
    comb(0, 1)


if __name__ == '__main__':
    main()