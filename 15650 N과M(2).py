import sys
<<<<<<< HEAD

def getSubsum(data) :
    '''
    n개의 숫자가 list로 주어질 때, 그 연속 부분 최대합을 반환하는 함수를 작성하세요.
    '''
    sum = 0
    res = -1e9
    for i in data:
        sum += i
        if sum < 0:
            sum = 0
            continue
        res = max(res,sum)
    return res
=======
read = sys.stdin.readline
global N, M, visited
def comb(cnt, start):
    if cnt == M:
        for i in range(1, N + 1):
            if visited[i]:
                print(i, end=' ')
        print()
        return
    for i in range(start, N + 1):
        visited[i] = True
        comb(cnt + 1, i + 1)
        visited[i] = False
>>>>>>> 363a7414a868f5273eb888715af9da62ae8902eb

def main():
    '''
    이 부분은 수정하지 마세요.
    '''
    n = int(input())
    data = [int(x) for x in input().split()]

    print(getSubsum(data))

if __name__ == "__main__":
    main()
