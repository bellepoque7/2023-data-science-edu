import sys
sys.setrecursionlimit(10 ** 6)
read = sys.stdin.readline

global V, E, parent, edges

def find_parent(a):
    # 자기 자신이 부모이면 최상단 노드임. 부모가 아니면 재귀로 계속 부모 탐색
    if a != parent[a]:
        parent[a] = find_parent(parent[a])
    # 부모이면 return
    return parent[a]


def union_parent(a, b):
    # 각자 자기 부모 찾기
    print('find_parnet',find_parent(a),find_parent(b))
    a = find_parent(a)
    b = find_parent(b)
    print(a,b)

    # 관례상 작은 쪽을 부모로 두는 경우가 많음
    if a < b:
        print('check2',a,b)
        parent[b] = a
    else:
        print('check3',a,b)
        parent[a] = b
    print('parent_list', parent)

def main():
    global V, E, parent, edges

    V, E = map(int, read().rstrip().split())

    # 부모를 자기 자신으로 초기화
    parent = [i for i in range(V + 1)]
    edges = []
    result = 0

    for _ in range(E):
        from_edge, to_edge, cost = map(int, read().rstrip().split())
        edges.append((cost, from_edge, to_edge))

    # 모든 간선들 비용 기준으로 오름차순
    edges.sort()
    # print('edges',edges)

    for edge in edges:
        cost, from_edge, to_edge = edge
        print('edge',edge)

        # 사이클이 생기지 않는 경우에만 union
        if find_parent(from_edge) != find_parent(to_edge):
            union_parent(from_edge, to_edge)
            result += cost

    print(result)


if __name__ == "__main__":
    main()


'''
3 3
0 2 1
0 3 4
2 3 2
'''