import sysㄴ
def binarySearch(data, m) :
    '''
    n개의 숫자 중에서 m이 존재하면 "Yes", 존재하지 않으면 "No"를 반환하는 함수를 작성하세요.
    '''

    if len(data) == 0 :
        return "No"
    elif len(data) == 1 :
        return "Yes" if data[0] == m else "No"

    start = 0
    end = len(data) -1
    mid = len(data) // 2
    while start <= end :
        mid = (start + end) // 2 # 3 ->4
        if data[mid] == m:
            return 'Yes'
        elif data[mid] < m:
            start = mid +1
        elif data[mid] > m:
            end = mid -1    
    return 'No'
    # 재귀로 수행하기
    # mid = len(data) // 2
    # if data[mid] == m :
    #     return "Yes"
    # elif data[mid] > m :
    #     return binarySearch(data[:mid], m)
    # else :
    #     return binarySearch(data[mid+1:], m)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''
    data = [int(x) for x in input().split()]
    m = int(input())ㄴㄴ
    print(binarySearch(data, m))

if __name__ == "__main__":
    main()