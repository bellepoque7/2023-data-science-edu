from heapq import *
import sys
read = sys.stdin.readline
INF = int(1e9)
# Edge, Vertex
global V, E, graph, distance


def dijkstra(start):
    global V, E, graph, distance
    # (거리, 노드)로 저장. 그래야 거리 순으로 오름차순 정렬 됨
    pq = []
    #힙 pq에 기본거리값(0)과 시작점(start)로 저장
    heappush(pq, (0, start))
    distance[start] = 0

    while len(pq) != 0:
        # 최단 거리가 가장 짧은 노드 pop(최소힙이기 때문에 pop으로 가능)
        dist, cur = heappop(pq)
        # 우선순위 큐에 저장된 현재 노드의 거리가 지금까지 저장된 최단 거리 보다 크면 무시. 이미 처리 되었다는 의미
        if distance[cur] < dist:
            continue

        for vertex, distance_to_cur in graph[cur]:
            # 현재 노드 거쳐서 vertex까지 이동하는 거리
            cost = dist + distance_to_cur
            # 현재 노드 거쳐서 가는 경우가 더 짧은 경우
            if cost < distance[vertex]:
                # 최단 거리 갱신
                distance[vertex] = cost
                # 우선순위 큐에 저장
                heappush(pq, (cost, vertex))


def main():
    global V, E, graph, distance
    V, E = map(int, read().rstrip().split())
    # 시작점 입력
    start = int(read().rstrip())
    # graph 초기화. 정점만큼만 있어야 됨
    graph = [[] for _ in range(V + 1)]
    # 최단 거리 테이블 무한으로 초기화. 정점에 대한 최단거리 이므로 정점 만큼 필요
    distance = [INF for _ in range(V + 1)]

    # 간선 정보 입력.
    for _ in range(E):
        # start부터 end까지 가는데 cost 만큼 걸림
        from_node, to_node, cost = map(int, read().rstrip().split())
        graph[from_node].append((to_node, cost))

    dijkstra(start)

    for i in range(1, V + 1):
        if distance[i] == INF:
            print("갈 수 없음")
        else:
            print(distance[i])


if __name__ == '__main__':
    main()


'''
input
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

output
0
2
3
1
2
4
'''