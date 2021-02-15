n = 14
m = 16
sym = '-'

# створення матриці
matrix = []
i = 0
while i < n:
    row = []
    j = 0
    while j < m:
        row.append(sym)
        j += 1
    matrix.append(row)
    i += 1


# виведення матриці
for row in matrix:
    row_text = '|'
    for el in row:
        row_text += str(el) + " "
    print(row_text[:-1] + "|")

