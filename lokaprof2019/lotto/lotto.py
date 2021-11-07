from typing import List, TextIO

ROW_NR_COUNT = 5
MIN = 1
MAX = 40

def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None

def get_filename():
    return input('Enter file name: ')

def read_lotto_rows(lotto_file: TextIO):
    rows = []
    for line in lotto_file:
        row = []
        for nr in line.split():
            row.append(int(nr))
        rows.append(row)
    
    #rows = [[int(nr) for nr in line.split()] for line in lotto_file]
    return rows

def get_winning_numbers():
    return input('Enter winning numbers: ').split()

def is_number_in_range(nr: int):
    return MIN <= nr <= MAX

def get_validated_winning_numbers(winning_numbers: List[str]):
    if (len(winning_numbers) == ROW_NR_COUNT):
        lotto_row = []
        for nr_string in winning_numbers:
            try:
                nr = int(nr_string)
                if is_number_in_range(nr):
                    lotto_row.append(nr)
                else:
                    return None
            except ValueError:
                return None
        return lotto_row
    else:
        return None

def get_lotto_row_string(lotto_row, winning_numbers):
    row_string = ''
    for lotto_number in lotto_row:
        row_string += str(lotto_number)
        if lotto_number in winning_numbers:
            row_string += '*'
        row_string += ' '
    return row_string

def display_lotto_row(lotto_row, winning_numbers):
    lotto_row_string = get_lotto_row_string(lotto_row, winning_numbers)
    print(lotto_row_string)

def display_lotto_rows(lotto_rows, winning_numbers):
    for row in lotto_rows:
        display_lotto_row(row, winning_numbers)  

filename = get_filename()
lotto_file = open_file(filename)
if lotto_file:
    lotto_rows = read_lotto_rows(lotto_file)
    winning_numbers = get_winning_numbers()
    validated_winning_numbers = get_validated_winning_numbers(winning_numbers)
    if validated_winning_numbers:
        display_lotto_rows(lotto_rows, validated_winning_numbers)
    else:
        print('Winning numbers are invalid!')
else:
    print(f'File {filename} not found!')
