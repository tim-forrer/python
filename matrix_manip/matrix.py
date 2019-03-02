def matrix_gen(n, m): #given 2 parameters, create a matrix of desired dimension
    matrix = []
    for i in range(n):
        new_row = []
        for j in range(m):
            new_row.append(int(input("What would you like as the %d row and %d column entry? " %(i + 1, j + 1))))
        matrix.append(new_row)
    return matrix

def formatted_matrix(mat): #returns a nice looking matrix
    for i in mat:
        print(i),
    return mat

def scalar_multiplication(mat, n):
    multiplied_mat = mat
    for i in multiplied_mat:
        multiplied_mat[i] *= n
    return multiplied_mat

def matrix_addition(matA, matB):
    final_matrix = []    
    for i in range(len(matA)):
        new_row = []
        for j in range(len(matA[0])):
            new_row.append(matA[i][j] + matB[i][j])
        final_matrix.append(new_row)
    return final_matrix

def matrix_subtraction(matA, matB):
    final_matrix = []    
    minus_matB = scalar_multiplication(matB, -1)
    final_matrix = matrix_addition(matA, minus_matB)
    return final_matrix

def transpose(mat):
    mat_transpose = [ [] for i in range(len(mat[0])) ]
    for i in range(len(mat_transpose)):
        for j in range(len(mat)):
            mat_transpose[i].append(mat[j][i])
    return mat_transpose

def dot_prod(vectA, vectB):
    final_value = 0
    for i in range(len(vectA)):
        final_value += vectA[i] * vectB[i]
    return final_value

def matrix_multi(matA, matB):
    final_matrix = [ [] for i in range(len(matA)) ]
    for i in range(len(final_matrix)):
        for j in range(len(matB[0])):
            final_matrix[i].append(dot_prod(matA[i], transpose(matB)[j]))
    return final_matrix