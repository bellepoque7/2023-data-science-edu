#https://velog.io/@kgorae/%EC%9D%B4%EC%BD%94%ED%85%8C-%EC%B5%9C%EB%8B%A8-%EA%B2%BD%EB%A1%9C-%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B0%9C%EB%85%90
import sys
from heapq import *
read = sys.stdin.readline

global V, E, graph, distance
INF = int(1e9)

# 다익스트라 그대로 사용
def dijkstra(start, end):
    global V, E, graph, distance
    pq = []
    heappush(pq, (0, start))
    distance[start] = 0

    while len(pq) != 0:
        #최단거리가 가장 짧은 노드의 정보 꺼내기
        #최소힙이니까 pop 하면 자연스럽게 가능
        dist, cur = heappop(pq)

        #현재 노드가 이미 처리된 적있는 노드라면 무시함
        if dist > distance[cur]:
            continue

        #현재노드와 연결된 인접한 노드를 확인
        for vertex, distance_to_cur in graph[cur]:
            cost = dist + distance_to_cur

            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 짧으면
            if cost < distance[vertex]:
                #업데이트
                heappush(pq, (cost, vertex))
                distance[vertex] = cost


def main():
    global V, E, graph, distance
    V = int(read().rstrip())   #노드의 갯수
    E = int(read().rstrip())   #간선 갯수

    #그래프의 정보. 인덱스에 (도착, 비용) 형태로 받을 예정
    graph = [[] for _ in range(V + 1)] 
    #최단거리 테이블 리스트
    distance = [INF for _ in range(V + 1)]

    for i in range(E):
        from_edge, to_edge, cost = map(int, read().rstrip().split())
        graph[from_edge].append((to_edge, cost))

    #출발과 도착지점 저장
    start, end = map(int, read().rstrip().split())

    dijkstra(start, end)

    print(distance[end])


if __name__ == '__main__':
    main()