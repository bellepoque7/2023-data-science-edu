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
    global N, M, visited
    N, M = map(int, read().rstrip().split())
    visited = [False for i in range(N + 1)]
    comb(0, 1)

if __name__ == '__main__':
    main()