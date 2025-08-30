def transpose_matrix(matrix):
    
    rows = len(matrix)
    columns = len(matrix[0])

          

    return [[matrix[i][j] for i in range(rows)] for j in range(columns)]



if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6]]
    print(transpose_matrix(matrix))