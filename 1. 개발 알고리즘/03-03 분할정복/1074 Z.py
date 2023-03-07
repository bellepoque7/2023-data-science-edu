import sys
read = sys.stdin.readline

global N, R, C, res, flag
def Z(r, c, size):
    global N, R, C, res, flag
    # 탈출조건: 원하는 위치를 찾은 경우(size ==1 일때)
    if r == R and c == C:
        #flag가 True가 되는 시점이 중요함.
        #size=1일때 찾으면 나머지 size=2,4,8...등에 대한 탐색은 그냥 다 안하는거임. 
        flag = True
        return

    # 현재 범위 내에 R, C가 존재 할 경우
    if r <= R < r + size and c <= C < c + size:
        # 크기를 쪼개서 재귀해 들어감.
        for nr, nc in [(r, c), (r, c + (size // 2)), (r + (size // 2), c), (r + (size // 2), c + (size // 2))]:
            # 결과가 안나온 경우 다음 위치로 재귀
            if not flag:
                Z(nr, nc, size // 2)
            # 결과가 나왔으면 종료
            else:
                return
    #현재 범위 내에 없으면 넓이 만큼 더해줌
    #탐색하지 않는대신 값을 추가해주는거임.
    else:
        res += size ** 2


def main():
    global N, R, C, res, flag
    N, R, C = map(int, read().rstrip().split())
    res = 0
    flag = False
    Z(0, 0, 2 ** N)
    print(res)


if __name__ == "__main__":
    main()
