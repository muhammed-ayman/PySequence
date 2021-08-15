def minimum_value(values_arr):  # getting the minimum number in values_arr (array)
    min_value = values_arr[0]
    for value in values_arr:
        if value < min_value:
            min_value = value

    return min_value  # returning the minimum value


def minimum_edit_distance(seq_one, seq_two):  # getting two string inputs representing two sequences

    # checking if one of the two sequences is empty and returning the other's length as the edit distance

    if not seq_one:
        return len(seq_two)
    if not seq_two:
        return len(seq_one)

    # representing the rows and columns with the first and the second sequences respectively

    rows = len(seq_one) + 1
    cols = len(seq_two) + 1
    edit_matrix = []  # the dynamic programming matrix for the edit distance

    # filling the edit matrix with 0s as the initial values

    for i in range(rows):
        edit_matrix_cols = []
        for j in range(cols):
            edit_matrix_cols.append(0)
        edit_matrix.append(edit_matrix_cols)

    # filling the initial values of the 1st row and the 1st column

    for i in range(1, rows):
        edit_matrix[i][0] = i
    for i in range(1, cols):
        edit_matrix[0][i] = i

    for i in range(1, rows):
        for j in range(1, cols):
            edit_count = 0
            if seq_one[i - 1] != seq_two[j - 1]:
                edit_count = 1

            # adding the minimum value of the matrix cells around (i,j) to the edit_count

            edit_count += minimum_value([edit_matrix[i][j - 1],
                    edit_matrix[i - 1][j], edit_matrix[i - 1][j - 1]])
            edit_matrix[i][j] = edit_count  # replacing the matrix(i,j) with the edit_count

    return edit_matrix[rows - 1][cols - 1]  # returning the edit distance as the last element in the edit matrix
