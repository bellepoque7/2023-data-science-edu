import sys

read = sys.stdin.readline
INF = 1e9


def main():
    V = int(read().rstrip())
    E = int(read().rstrip())

    # 이동 테이블 무한대로 초기화
    graph = [[INF for _ in range(V + 1)] for _ in range(V + 1)]

    # 자기 자신까지 가는 거리 0으로 저장
    for i in range(1, V + 1):
        graph[i][i] = 0

    for _ in range(E):
        start, end, cost = map(int, read().rstrip().split())
        graph[start][end] = min(cost, graph[start][end])
        
    for i in range(V):
        print(graph[i])

    for k in range(1, V + 1):
        for i in range(1, V + 1):
            for j in range(1, V + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, V + 1):
        for j in range(1, V + 1):
            if graph[i][j] == INF:
                print(0, end=' ')
            else:
                print(graph[i][j], end=' ')
        print()


if __name__ == '__main__':
    main()