#O(N**2)

def quadratic(n):
    for i in range(0,n):
        for j in range(0, n):
            print("This is quadratic")

#quadratic(2)

#O(N**3)

def cubic(n):
    for i in range(0,n):
        for j in range(0, n):
            for k in range(0,n):
                print("This is cubic")

cubic(2)
