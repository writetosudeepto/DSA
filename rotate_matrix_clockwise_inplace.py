def rotate_matrix_90(matrix):
    left,right = 0,len(matrix)-1
    while left < right:
        for i in range(right-left):
            top, bottom =  left, right
            topLeft = matrix[top][left+i] # save the top left to be used later
            matrix[top][left+i] = matrix[bottom-i][left] # move the bottom left to top left
            matrix[bottom-i][left] = matrix[bottom][right-i] # move the bottom right to bottom left
            matrix[bottom][right-i] = matrix[top+i][right] # move the top right to bottom right
            matrix[top+i][right] = topLeft # move the saved top left to top right
        left += 1
        right -= 1
a = [[1,2,3],[4,5,6],[7,8,9]]
rotate_matrix_90(a)
print(a)
