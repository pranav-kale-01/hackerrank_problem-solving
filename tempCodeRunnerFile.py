import math
import os
import random
import re
import sys
from turtle import st

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    d = {}

    for candel in candles:
        try:
            d[str(candel)] += 1 
            print("present")
        except:
            d[str(candel)] = 0 

            print ("not present")

if __name__ == '__main__':


    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
