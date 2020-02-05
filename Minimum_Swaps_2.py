https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):


    swaps=0

    arr = [i-1 for i in arr]

    for i in range(0, len(arr)-1):
    #     print('---------------------')
    #     print(i)
        while i != arr[i]:
            temp = arr[i]
            arr[i]=arr[temp]
            arr[temp]=temp
            swaps+=1
    return swaps

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
