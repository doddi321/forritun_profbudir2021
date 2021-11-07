from typing import List

BOOKED_CHARACTER = 'X'
MORE_SEATS = 'y'
NO_MORE_SEATS = 'n'

def initialize_seating(no_of_rows):
    ''' Returns an empty seating allocation: list of lists
        The seats in each row are marked with four letters, "A", "B", "C", "D"'''
    seating = []
    for _ in range(0, no_of_rows):
        seats = ['A','B','C','D']
        seating.append(seats)
    return seating 

def get_number_of_rows():
    return int(input('Enter number of rows: '))

def display_seats(seats: List[List[str]]):
    for row_index, row in enumerate(seats):
        row_string = f'{row_index + 1:>2}  ' + ' '.join(row) + ' '
        print(row_string)

def get_seat_number():
    row_nr, seat = input('Input seat number (row seat): ').split()
    return int(row_nr), seat

def index_of_seat(seat):
    return ord(seat) - ord('A')

def is_row_taken(seats, row_nr, seat):
    return seats[row_nr - 1][index_of_seat(seat)] == BOOKED_CHARACTER

def update_seats(seats, row_nr, seat):
    seats[row_nr - 1][index_of_seat(seat)] = BOOKED_CHARACTER

def get_more_seats():
    return input(f'More seats ({MORE_SEATS}/{NO_MORE_SEATS})? ')

def are_seats_available(seats):
    for row in seats:
        for seat in row:
            if seat != BOOKED_CHARACTER:
                return True 
    return False

nr_of_rows = get_number_of_rows()
seats = initialize_seating(nr_of_rows)
display_seats(seats)

cont = MORE_SEATS
while cont == MORE_SEATS:
        row_nr, seat = get_seat_number()
        if (not is_row_taken(seats, row_nr, seat)):
            update_seats(seats, row_nr, seat)
            display_seats(seats)
            if (are_seats_available(seats)):
                cont = get_more_seats()
            else:
                cont = NO_MORE_SEATS
        else:
            print('That seat is taken!')