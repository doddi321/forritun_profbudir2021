from typing import List, Text, TextIO
import math

def get_filename():
    return input('Enter file name: ')

def get_file(filename: str):
    try:
        return open(filename, 'r')
    except FileNotFoundError:
        return None

def get_grades(grades_file: TextIO):
    grades = []
    for line in grades_file:
        try:
            grades.append(float(line.strip()))
        except ValueError:
            pass

    return grades

def average(grades: List[float]):
    return sum(grades) / len(grades)

def standard_deviation(grades: List[float], average: float):
    grade_deviation = 0
    for grade in grades:
        grade_deviation += (grade - average)**2

    return math.sqrt(grade_deviation / len(grades)) 

def print_two_decimals(name, value):
    print(f'{name}: {value:.2f}')

filename =  get_filename()
grades_file = get_file(filename)
if grades_file:
    grades = get_grades(grades_file)
    average_grade = average(grades)
    std_dev_grades = standard_deviation(grades, average_grade)

    print_two_decimals("Average", average_grade)
    print_two_decimals("Standard deviation", std_dev_grades)

    grades_file.close()
else:
    print(f'File {filename} not found!')