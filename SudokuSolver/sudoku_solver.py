# Find method to generate sudoku board

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
ROWS, COLS = 9, 9


def print_board(bo):
    '''
    Description : Prints the board in the form of rows and columns, seperating each 3x3 grid
    Input : Sudoku board array
    Output : Prints board with grid lines
    '''
    for r in range(ROWS):
        if r % 3 == 0 and r != 0:
            print('- - - - - - - - - - - -')
            
        for c in range(COLS):
            if c % 3 == 0 and c != 0:
                print(' | ', end='')
                
            if c == (COLS - 1):
                print(bo[r][c])
            else:
                print(str(bo[r][c]) + ' ', end='')
                
def find_empty(bo):
    '''
    Description: Finds an empty cell to fill up
    Input : Sudoku baord array
    Output : Tuple of coordinates, like (row, column)
    '''
    for r in range(ROWS):
        for c in range(COLS):
            if bo[r][c] == 0:
                return (r, c)
            
    return None
               
def valid(bo, num, pos):
    '''
    Description: Checks if entered number is valid or not
    Input : bo - Sudoku board array
            num - The number being tried in the cell
            pos - the coordinate tuple returned by find_empty() function
    Output : 
    '''
    # Check row
    for c in range(COLS):
        if bo[pos[0]][c] == num and c != pos[1]:
            return False
    
    # Check column
    for r in range(ROWS):
        if bo[r][pos[1]] == num and r != pos[0]:
            return False
        
    # Check 3x3 grid
    grid_y_start = (pos[1] // 3) * 3 
    grid_x_start = (pos[0] // 3) * 3
    for r in range(grid_x_start, grid_x_start + 3):
        for c in range(grid_y_start, grid_y_start + 3):
            if bo[r][c] == num and pos != (r,c):
                return False
    
    return True    

def solve(bo):
    '''
    Description: Solves the Sudoku puzzle using backtracking algorithm 
    Input : Sudoku board array
    Output : returns True if board is filled; else False
    '''
    
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
        
    for num in range(1,10):
        if valid(bo, num, (row,col)):
            bo[row][col] = num
            
            if solve(bo):
                return True
            
            bo[row][col] = 0
            
    return False
        

print('Before solving: \n')
print_board(board)
print('\n')
    
solve(board)
    
print('After solving: \n')
print_board(board)
    