# Space complexity example one: O(1) - Constant

def sumUpTo(arr):
    sum = 0
    n = len(arr)
    for i in range(0,n):
        sum += arr[i]
    return sum

#print(sumUpTo([1,2,3,4]))

# Space complexity example two: O(N) - Linear

def getArrUpTo(n):
    arr =[]

    for i in range(0,n + 1):
        arr.append(i)
    return arr

print(getArrUpTo(4))
