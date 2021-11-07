ISBN_LENGTH = 13
SEPERATOR_INDEXES = [1, 5, 11]
SEPERATOR = '-'
EXIT = 'q'


def get_isbn():
    return input('Enter an ISBN: ')


def is_length_valid(isbn: str):
    return len(isbn) == ISBN_LENGTH


def are_seperators_in_correct_positions(isbn_string: str):
    seperator_counter = 0
    for index, char in enumerate(isbn_string):
        if char == SEPERATOR:
            seperator_counter += 1
            if index not in SEPERATOR_INDEXES:
                return False
    return len(SEPERATOR_INDEXES) == seperator_counter


def is_all_digit_or_seperators(isbn_string: str):
    for char in isbn_string:
        if char != SEPERATOR and not char.isdigit():
            return False
    return True


def is_isbn_valid(isbn_string: str):
    length_validation = is_length_valid(isbn_string)
    seperators_validation = are_seperators_in_correct_positions(isbn_string) 
    character_validation =  is_all_digit_or_seperators(isbn_string)

    return length_validation and seperators_validation and character_validation


def print_validation_result(is_valid):
    if is_valid:
        print('Valid format!')
    else:
        print('Invalid format!')


isbn_string = get_isbn()
while isbn_string != EXIT:
    validation_result = is_isbn_valid(isbn_string)
    print_validation_result(validation_result)
    isbn_string = get_isbn()
