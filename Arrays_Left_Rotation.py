# 
# 5 4
# 1 2 3 4 5 
# output: 5 1 2 3 4

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(arr, m):

    
    sub_arr = arr[0:m]
    final_arr = arr[m:]

    final_arr.extend(sub_arr)

    return final_arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

