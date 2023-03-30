#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    counter=0
    for n in grades:
        if n >= 38:
            p=n+5
            q=(5-(p % 5))
            if q < 3:
                grades[counter] = n + q
        counter+=1
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    
    while grades_count<0 or grades_count>60:
        grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        while grades_item < 0 or grades_item >100:
            grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
