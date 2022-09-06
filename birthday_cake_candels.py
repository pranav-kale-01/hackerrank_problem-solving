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
    d,max_n = {}, 0
    
    for candel in candles:
        if( candel > max_n ):
            max_n = candel

        try:
            d[str(candel)] += 1 
        except:
            d[str(candel)] = 1 

    return d[str(max_n)]

if __name__ == '__main__':


    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

