n = 5  # Number of rows for the triangle

for i in range(1, n + 1):  # Outer loop controls the number of rows
    for j in range(i):  # Inner loop prints stars for each row
        print("*", end="")  # print() function prints without a newline
    print()  # After finishing the inner loop, print a newline


rows=5
for i in range(1,rows + 1):
    print(i* "*")


2 Inverted Triangle Pattern:
n = 5  # Number of rows for the triangle
for i in range(n, 0, -1):  # Start from n and decrease to 1
    for j in range(i):  # Print i stars
        print("*", end="")
    print()  # Print new line
2)
rows=5
for i in range(rows,0,-1 ):
    print(i* "*")


