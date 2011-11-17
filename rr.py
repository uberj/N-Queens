# Rotation and Reflections functions
import copy
from nqueens import *

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
