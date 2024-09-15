
N = int(input("What should our countdown start at: "))

time_remaining = N
for time_passed in range(0,N+1):
    time_remaining = N - time_passed
    print(time_remaining, "minutes are left!")
    print(time_passed, "minutes have passed!")
    
    print()