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


#CHECK IF THE NUMBER IS VALID
def check_valid(bo, num , pos):

    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #check square
    box_row = pos[0]//3
    box_column = pos[1]//3
    for row in range((box_row)*3,box_row*3+3):
        for column in range((box_column)*3,box_column*3+3):
            if bo[row][column] == num and (row,column) != pos:
                return False
    return True

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if check_valid(bo,i,(row,col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    return False



def print_board(bo):
    for r in range(len(bo)):
        if r%3==0 and r!=0:
            print('-'*22)
        for c in range(len(bo[0])):
            if c%3==0 and c!=0:
                print('| ', end="")
            if c == 8:
                print(str(bo[r][c]))
            else:
                print(str(bo[r][c])+' ', end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)
    return None

print_board(board)
solve(board)
print('\nThis is the solved board')
print_board(board)
