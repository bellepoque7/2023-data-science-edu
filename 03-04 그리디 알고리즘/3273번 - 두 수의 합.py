import sys
read = sys.stdin.readline

def main():
    N = int(read().rstrip())
    a = list(map(int, read().rstrip().split()))
    x = int(read().rstrip())

    # 오름차순 정렬
    a.sort()
    left = 0
    right = N - 1
    res = 0

    while left < right:
        # 현재 가리키고 있는 값들 더하기
        sum = a[left] + a[right]
        # 더한 값이 x와 같은 경우 카운팅 하고 포인터 둘 다 이동
        if sum == x:
            res += 1
            left += 1
            right -= 1
        # 더한 값이 x보다 작은 경우 왼쪽 포인터만 이동
        elif sum < x:
            left += 1
        # 더한 값이 x보다 큰 경우 오른쪽 포인터만 이동
        else:
            right -= 1

    print(res)

if __name__ == "__main__":
    main()
