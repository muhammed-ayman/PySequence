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
    edit_matrix = [[0 for i in range(cols)] for j in range(rows)]  # the dynamic programming matrix for the edit distance

    # filling the initial values of the 1st row and the 1st column

    for i in range(1, rows):
        edit_matrix[i][0] = i
    for i in range(1, cols):
        edit_matrix[0][i] = i

    for i in range(1, rows):
        for j in range(1, cols):
            if seq_one[i - 1] != seq_two[j - 1]:
                # place 1 + the minimum value of the matrix cells around (i,j) in the matrix current position
                edit_count = 1 + minimum_value([edit_matrix[i][j - 1],
                        edit_matrix[i - 1][j], edit_matrix[i - 1][j - 1]])
                edit_matrix[i][j] = edit_count  # replacing the matrix(i,j) with the edit_count
            else:
                edit_matrix[i][j] = edit_matrix[i-1][j-1]

    return edit_matrix[rows - 1][cols - 1]  # returning the edit distance as the last element in the edit matrix
