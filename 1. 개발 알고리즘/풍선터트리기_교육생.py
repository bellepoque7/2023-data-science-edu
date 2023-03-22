'''
rotata 함수의 시간복잡도는 O(k)
for 문은 정직하게 O(n)

https://wiki.python.org/moin/TimeComplexity


Finding the element at position k in a doubly-linked list is O(k) time.
Rearranging the pointers may be constant-time, but you have to find the place where they should point first.
'''


from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    
    # N,M = map(int,input().split())
    # Q = deque()
    # num = list(map(int,input().split()))
    # for i in range(N):
    #     Q.append((i+1,num[i]))

    N = 4
    M = 4
    Q =  deque([[1, 9], [2, 8], [3, 9], [4, 9]])
    # Q =  deque([[1, 1], [2, 1]])
    # print(Q)
    ans = []
    while len(Q)>1:
        # print(len(Q))
        
        B,cnt = Q.popleft()
        cnt -= 1
        
        if cnt == 0:
            print(B, end=' ')
            ans.append(B)
        else:
            Q.append((B,cnt))
        
        for i in range(M):
            # print(0,Q)
            B,cnt = Q.popleft()
            Q.append((B,cnt))
            # print(Q)
            # print(1,Q)
    # print(Q)
    print(Q[0][0])
    # print(*ans)


if __name__ == '__main__':
    main()