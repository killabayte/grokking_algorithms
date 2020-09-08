def sumUpToN(n):
    sum = 0
    for i in range(0,n+1):
        sum += i
    return sum

result = sumUpToN(4)
print(result)
