# song.py
# This program outputs the lyrics to a user-generated song
a = input("What item would you like?   ")
b = input("Where is it?   ")
c = input("How is it removed?   ")
d = int(input("How many (whole number) verses should be performed?   "))
print("\nYour song is:", end="\n\n")
for i in range(d):
    print(d-i, a + "s", b)
    if i < d-1:
        print("Can you believe there are", d-i, a + "s", b+"!?")
    else:
        print("Can you believe there is", d-i, a, b+"!?")
    print(c)

    
    if i !=d-1:
        print(d-i-1, a + "s", b, end="\n\n")    
print("\n\nNow there are no", a + "s left :(")




