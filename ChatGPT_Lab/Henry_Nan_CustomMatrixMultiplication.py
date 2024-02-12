def custom_matrix_multiplication(matrix_a, matrix_b):
    """
    Performs a custom matrix multiplication where each element of the resulting matrix is computed by taking the dot
    product of a row from the first matrix with the corresponding column from the second matrix, but with the column
    indices swapped.

    Args:
    matrix_a (list of lists): The first matrix.
    matrix_b (list of lists): The second matrix.

    Returns:
    list: The result of the custom matrix multiplication.
    """
    result = []

    # Iterate over each row in matrix_a
    for row_index in range(len(matrix_a)):
        temp = 0
        
        # Iterate over each column in matrix_b
        for col_index in range(len(matrix_b[0])):
            # Calculate the dot product of the row from matrix_a and the corresponding column from matrix_b
            temp += matrix_a[row_index][col_index] * matrix_b[col_index][row_index]
        
        # Append the result of the dot product to the result list
        result.append(temp)

    return result
