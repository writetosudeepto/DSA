def transpose_matrix(A):
    col = len(A[0])
    row = len(A)
    new_matrix = []
    for i in range(col):
        new_matrix.append([])
        for j in range(row):
            new_matrix[i].append(A[j][i])
    return new_matrix

print(transpose_matrix([[1,2,3],[4,5,6],[7,8,9]]))