def read_row(sudoku_dict, row_num):
    while True:
        row = input(f'Enter row #{str(row_num)}: ')
        if row.isdigit() and row.find('0') == -1 and len(row) == 9:
            sudoku_dict[row_num] = row
            break
        else:
            print('Invalid input. Enter nine digits using numbers 1-9.')

sudoku_dict = {}

for i in range(1,10):
    read_row(sudoku_dict, i)

validate_list = [1,2,3,4,5,6,7,8,9]

# Check Horizontal
for i in range(1,10):
    line_list = list(sudoku_dict[i]).sort()
    if line_list == validate_list:
        continue
    else:
        break

print(sudoku_dict)