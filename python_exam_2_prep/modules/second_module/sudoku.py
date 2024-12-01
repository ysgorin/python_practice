def read_row(sudoku_dict, row_num):
    while True:
        row = input(f'Enter row #{str(row_num)}: ')
        if row.isdigit() and row.find('0') == -1 and len(row) == 9:
            sudoku_dict[row_num] = row
            break
        else:
            print('Invalid input. Enter nine digits using numbers 1-9.')

def check_grid(sudoku_dict, row_num, col_num, validate_list):
    for row in range(3):
        for col in range(3):
            grid_list = []
            grid_list.append(sudoku_dict[row_num+row][col_num+col])
    if grid_list.sort() == validate_list:
        return True
    else:
        return False

sudoku_dict = {}

for i in range(1,10):
    read_row(sudoku_dict, i)

validate_list = [1,2,3,4,5,6,7,8,9]

validate_flag = True
# while validate_flag:
#     # Check Horizontal
#     for i in range(1,10):
#         line_list = list(sudoku_dict[i]).sort()
#         if line_list == validate_list:
#             continue
#         else:
#             validate_flag = False
#             break
#     # Check Vertical
#     for y in range(9):
#         for i in range(1,10):
#             line_list = []
#             line_list.append(sudoku_dict[i][y])
#         if line_list.sort() == validate_list:
#             continue
#         else:
#             validate_flag = False
#             break
    
#     # # Check 3 x 3 grids
#     # if check_grid(sudoku_dict, 1, 0, validate_list) \
#     #     and check_grid(sudoku_dict, 4, 3, validate_list) \
#     #         and check_grid(sudoku_dict, 7, 6, validate_list):
#     #     break
#     # else:
#     #     validate_flag = False
#     #     break

if validate_flag:
    print('Yes')
else:
    print('No')
