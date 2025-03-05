# Break Statement Example
n = 2
while True:
    i = 1
    while i <= 16:
        print("%dX%d=%d\n" % (n, i, n * i))
        i += 1
    choice = int(input("Do You Want to Continue Printing the Table Press 0 for No:"))
    if choice == 0:
        print("Exiting the Program")
        break
    n += 1
print("Program Finished Successfully.")
