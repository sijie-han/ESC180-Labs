'''
 X | O | X
---+---+---
 O | O | X
---+---+---
   | X |
'''

import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")



def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
def coordinates(square_num):
    return [(square_num-1)//3,square_num%3 -1]
def put_in_board(board, mark, square_num):
    coord = coordinates(square_num)
    board[coord[0]][coord[1]] = mark
def make_random_move():
    put_in_board(board,mark,random.randint(1,9))
def get_free_square(board):
    res = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                res.append([i,j])
    return res
def is_row_all_marks(board, row_i, mark):
    if board[row_i][0] == board[row_i][1] == board[row_i][2] == mark:
        return True
    return False
def is_col_all_marks(board, col_i, mark):
    if board[0][col_i] == board[1][col_i] == board[2][col_i] == mark:
        return True
    return False
def is_win(board,mark):
    for i in range(3):
        if is_row_all_marks(board,i,mark) or is_col_all_marks(board,i,mark):
            return True

    return False

def comp_move(board,mark):
    for tryout in get_free_square(board):
        oppo = "X"
        put_in_board(board, mark, 3*tryout[0]+tryout[1]+1)
        if is_win(board,mark):
            return 0
        else:
            put_in_board(board, oppo, 3*tryout[0]+tryout[1]+1)
            if is_win(board,oppo):
                put_in_board(board, mark, 3*tryout[0]+tryout[1]+1)
                return 0
            else:
                put_in_board(board, " ", 3*tryout[0]+tryout[1]+1)
    tryout = random.choice(get_free_square(board))
    put_in_board(board, mark, 3*tryout[0]+tryout[1]+1)




if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)

    print("\n\n")

    count = 0
    while count<=8:
        if count%2 == 0:
            print("Please insert X")
            square_num = int(input("Now put in the location of the mark: "))
            put_in_board(board, "X", square_num)
            print_board_and_legend(board)
            if is_win(board,"X"):
                print("X won the game!")
                break
        else:
            print("Please insert O")
            comp_move(board,"O")
            print_board_and_legend(board)
            if is_win(board,"O"):
                print("O won the game!")
                break
        count += 1





