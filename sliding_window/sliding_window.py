def maxSum(arr, wsize):
    arraySize = len(arr)
    if arraySize <= wsize:
        print("Invalid input parameters")
        return -1

    window_sum = sum([arr[i] for i in range(wsize)])
    max_sum = window_sum

    for i in range(arraySize - wsize):
        window_sum = window_sum - arr[i] + arr[i+wsize]
        max_sum = max(window_sum,max_sum)

    return max_sum

arr = [80, -50, 90, 100, 37, 14]
k = 3
answer = maxSum(arr, k) #227
print(answer)

