#https://jinho-study.tistory.com/311

def binary_search(li, a):
    s, e = 0
    len(li)-1
    res = -1
    while s <= e:
        m = (s + e) // 2
        if li[m] < a:
            res = m
            s = m + 1
        else:
            e = m - 1
    return res
    
    
for _ in range(int(input())):
    N, M = map(int, input().split())
    a_list = sorted(list(map(int, input().split())))
    b_list = sorted(list(map(int, input().split())))
    cnt = 0
    for a in A:
        cnt += (binary_search(b_list, a_list) + 1)
    print(cnt)