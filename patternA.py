N = int(input("Enter a positive integer: "))

for i in range(1,N+1):
    for j in range(1,N+1):
        if j < N:
            print(j, end = " ")
        else: 
            print(j)
    