import sys

def getSubsum(data) :
    '''
    n개의 숫자가 list로 주어질 때, 그 연속 부분 최대합을 반환하는 함수를 작성하세요.
    '''
    sum = 0
    res = -1e9
    for i in data:
        sum += i
        if sum < 0:
            sum = 0
            continue
        res = max(res,sum)
    return res

def main():
    '''
    이 부분은 수정하지 마세요.
    '''
    n = int(input())
    data = [int(x) for x in input().split()]

    print(getSubsum(data))

if __name__ == "__main__":
    main()
