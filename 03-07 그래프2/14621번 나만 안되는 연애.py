#https://bbbyung2.tistory.com/m/89  (문제해설)
#https://chanhuiseok.github.io/posts/algo-33/ (크루스칼)
import sys
read = sys.stdin.readline

global V, E, edges, gender, parent
INF = int(1e9)


#union & find 구현
#union find: 서로소 집합을 표현하는 자료구조.
#union: 서로 다른 두 집합을 병합
#find: 집합원소가 어떤 집합(루트노드기준)으로 속해있는지 찾는 연산

# 재귀적으로 부모노드 찾기
def find_parent(a):
    global V, E, edges, gender, parent
    if a != parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]

#union 서로 루트노드를 비교해서 합병시키기
def union_parent(a, b):
    global V, E, edges, gender, parent
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def main():
    global V, E, edges, gender, parent
    V, E = map(int, read().rstrip().split())
    edges = []

    #각 위치인덱스의 노드의 부모(루트노드)를 저장할 리스트 
    parent = [i for i in range(V + 1)]
    # 성별 받을 리스트 추가
    gender = [0] + read().rstrip().split()

    #edges리스트에 (비용, 시작, 끝) 형태로 넣기
    for _ in range(E):
        from_node, to_node, cost = map(int, read().rstrip().split())
        edges.append((cost, from_node, to_node))

    edges.sort()

    res = 0
    # 경로의 길이가 V - 1개 만큼 나와야 됨
    cnt = 0

    for edge in edges:
        cost, from_node, to_node = edge
        # 조건1. 연결하려는 두 노드가 부모노드가 다르고 & 성별로 다르다면 gogo
        if find_parent(from_node) != find_parent(to_node) and gender[from_node] != gender[to_node]:
            union_parent(from_node, to_node)
            res += cost
            cnt += 1

    if cnt == V - 1:
        print(res)
    else:
        print(-1)

if __name__ == '__main__':
    main()