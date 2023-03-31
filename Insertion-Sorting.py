#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    x=arr[n-1]
    y=n-2
    for i in range(0,n-1):
        if arr[y] > x :
            arr[y+1] = arr[y]
        else:
            arr[y+1]=x
            print(*arr,sep=" ")
            break
        y-=1
        print(*arr,sep=" ")

    if arr[0]==arr[1]:
        arr[0]=x
        print(*arr,sep=" ")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
