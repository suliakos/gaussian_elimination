n = 0
m = 0

def row_coloumn_input():
    global m, n
    n = input("n = ")
    n = int(n)
    m = input("m = ")
    m = int(m)
    if n < 1 or n > 10 or m < 1 or m > 10:
        print("Both dimensions of the matrix must be between 1 and 10. Please try again.\n")
        row_coloumn_input()

print("Provide the dimensions of the matrix:")
row_coloumn_input()
if m > n:
    print("Since the number of rows is greater than the number of coloumns, Gaussian elimination can not be performed on this matrix. Please try again.\n")
    row_coloumn_input()

#The matrix is stored as nested list
matrix = []