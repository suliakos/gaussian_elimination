n = 0
m = 0

print("Provide the dimensions of the augmented matrix:")
while n <= 0 or m <= 0:
    n = input("n = ")
    n = int(n)
    if n <= 0:
        print("The matrix must have at least one column.\n")
        continue
    m = input("m = ")
    m = int(m)
    if m <= 0:
        print("The matrix must have at least one row.\n")
        continue

#The matrix is stored as nested list
matrix = []
i = 1
while i <= m:
    #the following command splits the input after each white space, converts each separated string into an integer, creates a list out of these, then assigns it to the variable "row"
    row = list(map(float, input(f"\nEnter the entries of row number {i} left of the line in the augmented matrix separated with spaces: ").split()))
    if len(row) == n:
        matrix.append(row)
        i += 1
    else:
        print(f"You need to enter exactly {n-1} entries.")

#The entry matrix[m][n] would be normally indexed as a_m+1,n+1
#Since we want to run down the diagonal starting from a_1,1 down to a_n-1,n-1, the for loop has to go from 0 to n-1-1+1 = n-1
for d in range(0,m-1):
    #we assume that the entries below matrix[d][d] are all zeroes unless evidence is found for the contrary
    FullZeroColumn = True
    #if the entry indexed a_d,d is 0, look for the closest non-zero entry in the same column then swap the two rows
    if matrix[d][d] == 0:   
        for i in range(d+1, m):
            if matrix[i][d] != 0:
                matrix[i], matrix[d] = matrix[d], matrix[i]
                FullZeroColumn = False
                break
    else:
        FullZeroColumn = False
    #if matrix[d][d] is zero and no row has been switched, that means every entry in the given column is a zero in which case we are done for this column
    if FullZeroColumn:
        continue
    #if an entry below and in the same column as matrix[d,d] is not zero, determine the ratio of that entry and matrix[d,d], then subtract the ratio multiple of each entry in list d in the nested list not left of matrix[d,d] from each corresponding entry in the list not left of the list the aforementioned entry is in
    for i in range(d+1, m):
        ratio = matrix[i][d] / matrix[d][d]
        for j in range(d, n):
            matrix[i][j] -= ratio * matrix[d][j]

#round entries:
for i in range(0,m):
    for j in range(0,n):
        matrix[i][j] = round(matrix[i][j], 2)
        if (matrix[i][j] % 1) == 0:
            matrix[i][j] = round(matrix[i][j])
        elif (matrix[i][j] * 10) % 1 == 0:
            matrix[i][j] = round(matrix[i][j], 1)        

print("\nThis is the matrix in row echelon form:\n")

lengths = []

#stores the number that takes up the most space when displayes for each column  
for i in range(0,n):
    lengths.append(max(len(str(matrix[j][i])) for j in range(0,m)))
for i in matrix:
    for j in range(0,n):
        #prints the number, then adds enough spaces to be displayed in the same column as the "longest" number in that column then adds another space
        print(i[j], end="")
        for k in range(0,lengths[j]-len(str(i[j]))+1):
            print(" ", end="")
    print("\n")