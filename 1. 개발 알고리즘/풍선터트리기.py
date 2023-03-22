from collections import deque
# _, m = map(int, input().split())
# d = deque([i, baloon] for i, baloon in enumerate(map(int, input().split()), 1))
m = 4
d =  deque([[1, 9], [2, 8], [3, 9], [4, 9]])
# d = deque([[1, 1], [2, 1]])
# print(d)
# deque([[1, 1], [2, 4], [3, 2], [4, 3]])
res = []

while d:
    # print(d)
    d[0][1] -= 1

    if d[0][1] == 0:
        res.append(d.popleft()[0])
    else:
        #왼쪽으로 1씩
        d.rotate(-1)
        # print('rotate -1', d)
    #왼쪽으로 2씩
    d.rotate(-m)
    # print('rotate -m',d)
    
print(*res)