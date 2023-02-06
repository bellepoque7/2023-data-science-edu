import sys
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

def main():
    '''
    이 부분은 수정하지 마세요.
    '''
    n = int(input())
    data = [int(x) for x in input().split()]

    print(getSubsum(data))

if __name__ == "__main__":
    main()
