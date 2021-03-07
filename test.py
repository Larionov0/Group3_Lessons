def change_matrix(matrix):
    for row in matrix:
        for i, number in enumerate(row):
            if number % 2 == 1:
                row[i] = number * 2
            else:
                row[i] = number / 2


matrix = [[2, 6, 8],
          [6, 9, 5],
          [7, 3, 1]]

change_matrix(matrix)

print(matrix)

