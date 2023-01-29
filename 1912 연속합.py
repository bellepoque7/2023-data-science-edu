import sys

def getSubsum(data) :
    '''
    n개의 숫자가 list로 주어질 때, 그 연속 부분 최대합을 반환하는 함수를 작성하세요.
    '''
    my_sum = []
    n = int(input())
    n = len(data)
    for i in range(2,n+1): #2부터 8까지 반복
        for j in range(0,n-i+1):
            if j == n-i:
                my_sum.append(sum(data[j:]))
            else:
                my_sum.append(sum(data[j:j+i])) 
    # print(my_sum)
    return max(my_sum)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''
    data = [int(x) for x in input().split()]

    print(getSubsum(data))

if __name__ == "__main__":
    main()
