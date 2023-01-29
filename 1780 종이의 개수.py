def division(start_row, start_col, size):
    global minus_cnt, zero_cnt, one_cnt

    flag = 1
    num = arr[start_row][start_col]

    for row in range(start_row, start_row + size):
        for col in range(start_col, start_col + size):
            if num != arr[row][col]:
                flag = 0
                break

        if not flag:
            break

    if flag:
        if num == -1:
            minus_cnt += 1
        elif num == 0:
            zero_cnt += 1
        else:
            one_cnt += 1
    else:
        size //= 3
        division(start_row, start_col, size)
        division(start_row + size, start_col, size)
        division(start_row, start_col + size, size)
        division(start_row + size, start_col + size, size)
        division(start_row, start_col + size * 2, size)
        division(start_row + size * 2, start_col, size)
        division(start_row + size, start_col + size * 2, size)
        division(start_row + size * 2, start_col + size, size)
        division(start_row + size * 2, start_col + size * 2, size)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

minus_cnt = 0
zero_cnt = 0
one_cnt = 0

division(0, 0, n)

print(minus_cnt)
print(zero_cnt)
print(one_cnt)