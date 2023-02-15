import heapq
def find_mid(nums) :
    '''
    n개의 정수들을 담고 있는 배열 nums가 매개변수로 주어집니다.
    nums의 각 정수들이 차례대로 주어질 때, 매 순간마다 
    "지금까지 입력된 수 중에서 중간값"을 리스트로 저장하여 반환하세요.
    '''
    '''
    우린 최대힙의 루트노드를 중간값을로 설정할 것

    1. 입력될 수가 최대힙의 루트노드 이상이면 최소힙으로 
    그렇지 않다면 최대힙으로 넣는다. 
    2. 만약 전체 갯수가 홀수개면, 최소힙 -> 최대힙 이동
    '''
    n =  len(nums)    
    result = []

    max_heap = [] # 최대 힙(전체갯수가 홀수개이면 최대힙이 1개 더 많다. )
    min_heap = [] # 최소 힙
    for i in range(n):
        x = nums[i]

        if not max_heap or not min_heap: #둘중 하나라도힙이 비어져있으면
            heapq.heappush(max_heap,-x) # 최대힙이니까 -로 넣기 
        else: 
            #그렇지않으면 최대힙의 루트노트보다 큰지 작은지 비교
            if x >= - max_heap[0]:
                heapq.heappush(min_heap,x)
            else:
                heapq.heappush(max_heap,-x)
        #두 힙의 크기를 조정
        #자료의 갯수가 짝수면 len(left) == len(right)
        #자료의 갯수가 홀수면 len(left) + 1 === len(right)

        #정상적인 2가지 상태가 아니라면 while문 안을 실행해서 조정해주겠다.
        if not(len(max_heap)==len(min_heap) or len(max_heap) == len(min_heap) + 1):
            #left이 들고있는 갯수가 right의 갯수보다 2개 이상이면
            if len(max_heap) > len(min_heap):
                #left에서 값을 뽑아서 right에 넣어야한다. 
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            #right이 들고있는 갯수가 left보다 많다면
            else:
                #right에서 값을 뽑아서 left에 넣는다.
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

        result.append(-max_heap[0])
    return result