


N = int(input("provide an integer to countdown from: "))

for time_passed in range(N, -1,-1):
    time_remaining = N - time_passed
    print(time_passed, "minutes are left!")
    print(time_remaining, "minutes have passed!")
    print()
