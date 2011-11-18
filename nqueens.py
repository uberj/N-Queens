import sys
import pdb
import unittest
import copy
import pprint
from board_utils import *
from rr import *

pp = pprint.PrettyPrinter(indent=4)

"""
Solve nqueens for a generic NxN board
"""
solutions = []
def solve_nqueens( n ):
    board = [ [0]*n for i in range(n) ]
    state = []
    do_nqueens( 0, n, board, state )

"""
Helper function.
"""
def do_nqueens( row, n, board, state ):
    if row >= n:
        solutions.append(copy.deepcopy(state))
        return
    for col in range(n):
        if valid_move( row, col, board, n ):
            mark( row, col, board )
            state.append((row,col))
            # Again!
            do_nqueens( row+1, n, board, state )
            unmark( row, col, board )
            state.remove((row,col))

def mark( row, col, board ):
    board[row][col] = 1

def unmark( row, col, board ):
    board[row][col] = 0

"""
Check a generic (row,col) coordinate to see if it is a
valid move.
"""
def valid_move( row, col, board, n ):
    col_val = check_col( row, col, board, n )
    diags_val = check_diags( row, col, board, n )
    return not (col_val or diags_val)


"""
Generic test for board state. Control via xd and yd (x-direction and y-direction).
"""
def check_dir( row, col, xd, yd, board, n ):
    if row < 0 or col < 0 or row >= n or col >= n:
        return False
    else:
        if board[row][col]:
            return True
        else:
            return check_dir( row + xd, col + yd, xd, yd, board, n )
"""
Check a row for move.
True if there is a move.
False if the colomn is free.
"""
def check_diags( row, col, board, n ):
    up_left = check_dir( row, col, 1, 1, board, n )
    up_right = check_dir( row, col, 1, -1, board, n )
    down_left = check_dir( row, col, -1, 1, board, n )
    down_right = check_dir( row, col, -1, -1, board, n )
    return up_left or up_right or down_left or down_right

"""
Check a column for move.
True if there is a move.
False if the colomn is free.
"""
def check_col( row, col, board, n):
    left = check_dir( row, col, 1, 0, board, n )
    right = check_dir( row, col, -1, 0, board, n )
    return left if left else right

"""
Check a row for move.
True if there is a move.
False if the colomn is free.
"""
def check_row( row, col, board, n ):
    up = check_dir( row, col, 0, 1, board, n )
    down = check_dir( row, col, 0, -1, board, n )
    return up if up else down

# Print board
def pb( board, n ):
    print "======================="
    for i in range(n):
        for j in range(n):
            print board[i][j],
        print



if __name__ == "__main__":
    n = int(sys.argv[1])
    solve_nqueens(n)
    meta_solutions = []
    uniq_solutions = []
    for solution in solutions:
        s_board = coord_to_board(solution)
        if solution not in meta_solutions:
            uniq_solutions.append(solutions)
            meta_solutions += gen_all_rr(s_board,n)
            meta_solutions.append(solution)

    print "There were %s unique solutions for a %s x %s board." % (len(uniq_solutions),n,n)

