import sys
sys.setrecursionlimit(10 ** 6)
read = sys.stdin.readline

global V, E, parent


def find_parent(a):
    global V, E, parent
    # 자기 자신이 부모이면 최상단 노드임. 부모가 아니면 재귀로 계속 부모 탐색
    if a != parent[a]:
        parent[a] = find_parent(parent[a])
    # 부모이면 return
    return parent[a]


def union_parent(a, b):
    global V, E, parent
    # 각자 자기 부모 찾기
    a = find_parent(a)
    b = find_parent(b)

    # 관례상 작은 쪽을 부모로 두는 경우가 많음
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def main():
    global V, E, parent

    V, E = map(int, read().rstrip().split())

    # 부모를 자기 자신으로 초기화
    parent = [i for i in range(V + 1)]

    # 부모 관계 정리
    for _ in range(E):
        a, b = map(int, read().rstrip().split())
        union_parent(a, b)

    # 각 노드가 포함된 집합 출력하여 확인하기
    print("각 노드가 포함된 집합:", end=' ')
    for i in range(1, V + 1):
        print(find_parent(i), end=' ')


if __name__ == "__main__":
    main()

'''
input
6 4
1 4
2 3
2 4
5 6

output
각 노드가 포함된 집합: 1 1 1 1 5 5
'''