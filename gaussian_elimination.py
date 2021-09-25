n = 0
m = 0

print("Provide the dimensions of the matrix:")
while n < 2 or n > 10 or m < 2 or m > 10:
    n = input("n = ")
    n = int(n)
    m = input("m = ")
    m = int(m)
    if n < 2 or n > 10 or m < 2 or m > 10:
        print("Both dimensions of the matrix must be between 2 and 10.\n")

#The matrix is stored as nested list
matrix = []
i = 1
while i <= m:
    row = list(map(int, input(f"\nEnter the values of row number {i} separated with spaces: ").split()))
    if len(row) == n:
        row.append(int(input("Enter the term right of the line in the augmented matrix: ")))
        matrix.append(row)
        i += 1
    else:
        print(f"You need to enter exactly {n} values.")

print(matrix)