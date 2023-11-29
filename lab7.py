L = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
def func():
    L[0] = [1,0,0]
    L[0][0]= 4
#func()
#print(L)


def modify(L):
    L = L[:]
    L[0] = [0,0,0]
    print(L)
modify(L)
print(L)



def is_sq_in_board(board, y, x):
    return x < len(board[0]) and y < len(board) and x>=0  and y >=0





def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x

def is_seq_complete(board, col, y_start, x_start, length, d_y, d_x):
    if not is_sq_in_board(board, y_start-d_y, x_start-d_x) or board[y_start-d_y][x_start-d_x] == col:
        return False
    if not is_sq_in_board(board, y_start+d_y*length, x_start+d_x*length) or board[y_start+d_y*length][x_start+d_x*length] == col:
        return False
    for i in range(length):
        if board[y_start+i*d_y][x_start+i*d_x] != col:
            return False
    return True



