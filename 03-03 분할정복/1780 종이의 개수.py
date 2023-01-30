import sys
read = sys.stdin.readline

''' 재귀순서
paper(1,1,9)
-> paper(1,1,3), paper(4,1,3), paper(1,4,3), paper(4,4,3), paper(1,7,3), paper(4,7,3)
위에 6개는 종료

-> paper(7,1,3), paper(7,4,3), paper(7,7,3)은 다시 9개씩 분화(즉, 1개씩 모두 리턴하여 size ==1 탈출조건 도달
'''

global N, a, res
def paper(r, c, size):
    global N, a, res
    # 탈출 조건
    if size == 1:
        # 종이 카운팅
        res[a[r][c] + 1] += 1
        return

    for i in range(r, r + size):
        for j in range(c, c + size):
            if a[i][j] != a[r][c]:
                # (1,4)를 찍는 순간 a[0][0]과 달라지므로 
                # 모든값을 3등분해서 다시 paper 찍어보기
                # 세로 삼등분
                for i in range(3):
                    # 가로 삼등분
                    for j in range(3):
                        paper(r + (size // 3 * i), c + (size // 3 * j), size // 3)
                return
    # 모두 같은 색이었을 경우 처리
    #값이 -1이면 0인덱스에 0이면 1인덱스에 1이면 2 인덱스에 넣어 순서대로 출력하면 답
    res[a[r][c] + 1] += 1

def main():
    global N, a, res
    N = int(read().rstrip())
    a = [[]]
    for i in range(N):
        temp = list(map(int, read().rstrip().split()))
        a.append([0] + temp)
    res = [0 for i in range(3)]
    paper(1, 1, N)
    for i in res:
        print(i)


if __name__ == '__main__':
    main()

