n = 0
m = 0

print("Provide the dimensions of the matrix:")
while n < 2 or n > 10 or m < 1 or m > 10:
    n = input("n = ")
    n = int(n)
    m = input("m = ")
    m = int(m)
    if n < 2 or n > 10 or m < 1 or m > 10:
        print("Both dimensions of the matrix must be between 2 and 10.\n")

#The matrix is stored as nested list
matrix = []
i = 1
while i <= m:
    #the following command splits the input after each white space, converts each separated string into an integer, creates a list out of these then assigns it to the variable "row"
    row = list(map(int, input(f"\nEnter the entries of row number {i} left of the line in the augmented matrix separated with spaces: ").split()))
    if len(row) == n-1:
        row.append(int(input("Enter the entry right of the line in the augmented matrix: ")))
        matrix.append(row)
        i += 1
    else:
        print(f"You need to enter exactly {n-1} entries.")

print(matrix)

#The entry matrix[m][n] would be normally indexed as a_m+1,n+1
#Since we want to run down the diagonal starting from a_1,1 down to a_n-1,n-1, the for loop has to go from 0 to n-1-1+1 = n-1
for d in range(0,m-1):
    #if the entry indexed a_d,d is 0, look for the closest non-zero entry in the same coloumn then swap the two rows
    if matrix[d][d] == 0:
        for i in range(d+1, m):
            if matrix[i][d] != 0:
                matrix[i], matrix[d] = matrix[d], matrix[i]
                break
    #if an entry below and in the same coloumn as matrix[d,d] is not zero, determine the ratio of that entry and matrix[d,d], then subtract the ratio multiple of each entry in list d in the nested list not left of matrix[d,d] from each corresponding entry in the list not left of the list the aforementioned entry is in
    for i in range(d+1, m):
        if matrix[i][d] != 0:
            ratio = int(matrix[i][d] / matrix[d][d])
            for j in range(d, n):
                matrix[i][j] -= ratio * matrix[d][j]
    
print(matrix)

