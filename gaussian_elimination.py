n = 0
m = 0

def row_coloumn_input():
    global m, n
    n = input("n = ")
    n = int(n)
    m = input("m = ")
    m = int(m)
    if n < 2 or n > 10 or m < 2 or m > 10:
        print("Both dimensions of the matrix must be between 1 and 10.\n")
        row_coloumn_input()

print("Provide the dimensions of the matrix:")
row_coloumn_input()
if n > m:
    print("Since the number of rows is greater than the number of coloumns, Gaussian elimination can not be performed on this matrix.\n")
    row_coloumn_input()

#The matrix is stored as nested list
matrix = []

def row_input(num_of_coloumns):
    row = list(map(int, input(f"Enter the values separated with spaces: ").split()))
    if len(row) != num_of_coloumns:
        print(f"You need to enter exactly {num_of_coloumns} values.\n")
        print(row)
        row_input(num_of_coloumns)
    else:
        return(row)

def matrix_input(num_of_rows, num_of_coloumns):
    global matrix
    for i in range(1, num_of_rows + 1):
        print(f"\nRow number {i}:")
        matrix.append(row_input(num_of_coloumns))
        print(matrix)