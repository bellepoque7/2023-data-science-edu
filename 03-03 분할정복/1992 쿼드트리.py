import sys
read = sys.stdin.readline

global N, a
def quad_tree(r, c, size):
    # 탈출 조건. 한 개밖에 없으면 그냥 출력하면 됨
    if size == 1:
        print(a[r][c], end='')
        return
    for i in range(r, r + size):
        for j in range(c, c + size):
            # 하나라도 안맞는게 나온 경우
            if a[r][c] != a[i][j]:
                print("(", end='')
                # 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래로 나눠서 체크
                quad_tree(r,c,size//2)
                quad_tree(r,c+(size // 2),size//2)
                quad_tree(r+(size // 2),c,size//2)
                quad_tree(r+(size // 2),c+(size // 2),size//2)
                # 한번이라도 안맞은 시점에서 나눠서 따로 출력 하므로 지금 크기에서 할 작업은 없음
                print(")", end='')
                return
    # 만약 여기까지 왔다면 모두 다 같은 숫자라는 의미
    print(a[r][c], end='')

def main():
    global N, a
    N = int(read().rstrip())
    # 인덱스 1부터 사용하기 위해
    a = [[]]

    for i in range(N):
        temp = list(map(int, read().rstrip()))
        a.append([0] + temp)

    quad_tree(1, 1, N)



if __name__ == '__main__':
    main()