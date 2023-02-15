from heapq import *

def main():
    max_heap = []
    min_heap = []

    n = int(input())
    temp = list(map(int, input().split()))

    for t in temp:
        #일단 최소힙에 밀어넣기
        heappush(min_heap, t)
        # 만약 최소힙이 더 길다면 균형맞추기
        if len(max_heap) < len(min_heap):
            heappush(max_heap, (-min_heap[0], min_heap[0]))
            heappop(min_heap)
        #둘다 있는데 최대힙의 실제값이 최소힙값보다 크다면 정렬이 안된 것이므로
        # 이동하기
        if len(max_heap) and len(min_heap) and max_heap[0][1] > min_heap[0]:
            a, b = max_heap[0][1], min_heap[0]
            heappop(max_heap)
            heappop(min_heap)
            heappush(max_heap, (-b, b))
            heappush(min_heap, a)
        #print('max_heap', max_heap , 'min_heap', min_heap)
        print(max_heap[0][1], end=" ")



if __name__ == "__main__":
    main()