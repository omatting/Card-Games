
N = int(input("What should our countdown start at: "))

time_passed = 0
time_remaining = N

for i in range(0, N+1):
    print(time_remaining, "minutes are left!")
    print(time_passed, "minutes have passed!")
    time_passed = time_passed + 1
    time_remaining = N - time_passed
    print()
    