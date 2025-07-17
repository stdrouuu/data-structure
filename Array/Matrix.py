def create_Mtx2D(row, col):
    mtx = []
    for i in range(row):
        rw = []
        for j in range(col):
            m = i + 1
            n = j + 1
            element = int(input("Enter [" + str(m) + "][" + str(n) + "]: "))
            rw.append(element)
        mtx.append(rw)
    return mtx
#tambahkan fungsi buat perkalian matrix
# def add_Mtx2D(mtx1, mtx2):
#     rw, cl = (len(mtx1), len(mtx1[0]))
#     mtx = [[0]* cl]*rw
#     mtx = [[mtx1[i][j] + mtx2[i][j] for j in range(cl)] for i in range(rw)] --> kotak katik ini utk perkalian
#     return mtx
def multiply_Mtx2D(mtx1, mtx2):
    row, col = (len(mtx1), len(mtx2))
    result = [[0] * col for _ in range(row)]

    for i in range((row)):
        for j in range(col):
            for k in range(len(mtx1)):
                result[i][j] += mtx1[i][k] * mtx2[k][j]
    return result

def print_Mtx2D(mtx):
    for row in mtx:
        print(row)    
    
def add_Mtx2D(mtx1, mtx2):
    rw, cl = (len(mtx1), len(mtx1[0]))
    mtx = [[0]* cl]*rw
    mtx = [[mtx1[i][j] + mtx2[i][j] for j in range(cl)] for i in range(rw)]
    return mtx

row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
print("Enter first matrix: ")
mtx1 = create_Mtx2D(row, col)
print("Enter second matrix: ")
mtx2 = create_Mtx2D(row, col)

print("First matrix: ")
print_Mtx2D(mtx1)
print("Second matrix: ")
print_Mtx2D(mtx2)
print("Result matrix: ")
mtx = add_Mtx2D(mtx1, mtx2)
print_Mtx2D(mtx)

#matrix perkalian
print("Result multiplied matrix:")
multiply = multiply_Mtx2D(mtx1, mtx2)
print_Mtx2D(multiply)
#output-----------------------------------
# Enter number of rows: 2
# Enter number of columns: 2
# Enter first matrix: 
# Enter [1][1]: 1
# Enter [1][2]: 2
# Enter [2][1]: 3
# Enter [2][2]: 4
# Enter second matrix: 
# Enter [1][1]: 1
# Enter [1][2]: 2
# Enter [2][1]: 3
# Enter [2][2]: 4

# First matrix: 
# [1, 2]
# [3, 4]
# Second matrix:
# [1, 2]
# [3, 4]
# Result matrix:
# [2, 4]
# [6, 8]
# Result of multiplication:
# [7, 10]
# [15, 22]
