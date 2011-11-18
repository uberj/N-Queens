# Rotation and Reflections functions
import copy
from nqueens import *
from board_utils import *

def rotate90(matrix, n):
    # OH GOD THIS IS TERRIBLE.
    rotated_matrix = copy.deepcopy(matrix)
    for i in range(n):
        for j in range(n):
            rotated_matrix[n-1-j][i] = matrix[i][j]
    return rotated_matrix

def reflect(matrix,n):
    reflected_matrix = []
    for i in range(n):
        reflected_matrix.append(copy.deepcopy(matrix[n-1-i]))

    return reflected_matrix

"""
Generate all rotations.
"""
def gen_all_rot(matrix,n):
    rote90 = rotate90(matrix,n)
    rote180 = rotate90(rote90,n)
    rote270 = rotate90(rote180,n)
    rots = [board_to_coord(rote90,n),\
            board_to_coord(rote180,n),\
            board_to_coord(rote270,n)]
    return rots

"""
Generate all rotations and reflections
"""
def gen_all_rr(matrix,n):
    reflected = reflect(matrix,n)
    rrs = []
    return gen_all_rot(matrix,n)+gen_all_rot(reflected,n)+[board_to_coord(reflect(matrix,n),n)]

