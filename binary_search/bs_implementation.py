def binarySearch(arr, target):
    left = 0
    right = len(arr)-1

    while(left <= right):
        mid = (left+right)//2 #0 9 = (0+9)//2 = 4

        if (arr[mid] == target):
            return mid
        elif (arr[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]

target = 9

result = binarySearch(arr, target) # index of the target: 5

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in the array")
