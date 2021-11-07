from os import read
from typing import List, TextIO


def open_file(file_name): # Do not change this line
    try:
        return open(file_name, 'r')
    except FileNotFoundError:
        return None
    
def read_matrix(file_object: TextIO): # Do not change this line
    return [[int(nr) for nr in row.split()] for row in file_object]
    

def row_sum_same(matrix: List[List[int]]): # Do not change this line
    '''Returns the sum of the elements in each row of the matrix if the sum is the same, else 0'''
    row_sum = sum(matrix[0])
    for row in matrix:
        if row_sum != sum(row):
            return 0 
    return row_sum

def transform_matrix(matrix: List[List[int]]):
    transformed_matrix = []
    for col_index in range(len(matrix)):
        flipped_column = []
        for row in matrix:
            flipped_column.append(row[col_index])

        transformed_matrix.append(flipped_column)
    return transformed_matrix

def col_sum_same(matrix: List[List[int]]): # Do not change this line
    '''Returns the sum of the elements in each column of the matrix if the sum is the same, else 0'''
    transformed_matrix = transform_matrix(matrix)
    return row_sum_same(transformed_matrix)

def print_matrix(matrix):
    for row in matrix:
        for nr in row:
            print(nr, end='\t')
        print()

def get_filename():
    return input('File name: ')

def is_sum_same(matrix):
    col_sum = col_sum_same(matrix)
    row_sum = row_sum_same(matrix)
    return col_sum == row_sum and col_sum != 0

def print_result(result: bool):
    if (result):
        print('Same sums')
    else:
        print('Not same sums')

def main(): # Do not change this line
    filename = get_filename()
    matrix_file = open_file(filename)
    if matrix_file:
        matrix = read_matrix(matrix_file)
        print_matrix(matrix)
        print_result(is_sum_same(matrix))
    else: 
        print('File not found')

# Main program starts here. Do not change it.
if __name__ == "__main__":
    main()