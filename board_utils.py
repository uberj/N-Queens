
"""
Convert a board (matrix) into
and array with vectors to note
where the queens were.
"""
def board_to_coord(board, n):
    vecs = []
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                vecs.append((i,j))
    return vecs

"""
Given a board (in matrix form). Check to see if it is
contained in the group of boards.
@return True if the board isn't in boards
        False if the board *is* in boards
"""
def check_for_board(boards, board):
    board_vec = board_to_coord(board)
    if board_vec in boards:
        print "Duplicate"
        return False
    else:
        print "Unique"
        return True

def coord_to_board(vec):
    n = len(vec)
    board = [ [0]*n for i in range(n) ]
    for i in range(len(vec)):
        for j in range(len(vec)):
            if (i,j) in vec:
                board[i][j] = 1
            else:
                continue
    return board

def pbc(vec):
    print "============"
    for i in range(len(vec)):
        for j in range(len(vec)):
            if (i,j) in vec:
                print '1',
            else:
                print '0',
        print
