
def min_switches(arr):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    switches = [0] * n
    
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + (arr[i] == i + 1)

    print(prefix_sum) #[0, 1, 2, 3, 4, 4, 4]
    
    for i in range(n):

        left_count = prefix_sum[i]
        right_count = i + 1 - left_count
        print(i,left_count,right_count)
        switches[i] = right_count - left_count
    
    return abs(sum(switches))

min_switches([1, 2, 3, 4, 2, 1])