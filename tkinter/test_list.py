rows = [["C", "CE"], [7, 8, 9, "+"], [4, 5, 6, "-"], [1, 2, 3, "*"], [0, "=", "/"]]
for i, row in enumerate(rows):
    print("Row", i, end=': ')
    for j, col in enumerate(row):
        print(col, ' ', end='')
    print('')