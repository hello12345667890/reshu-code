n = int(input("Please enter the number of rows.") )
for i in range(1,n+1):
    print("*"*i)



h = int(input("Please enter the amount of rows you want."))
for i in range(h,0,-1):
    print("*"*i)



n = int(input("Enter the number of rows for the diamond pattern: "))
# Upper half
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

