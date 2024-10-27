def square_pattern(n):
    for i in range (0,n):
        if i == 0 or i == n-1:
            print("X" * n)
        else:
            print("x" + " " * (n-2) + "X")
                    

n = int(input())
square_pattern(n)