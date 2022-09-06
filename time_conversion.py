import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    l = s[:-2].split(":", 1 )
    if( s[-2] == "A"):
        return ":".join( ["00"] + l[1:] ) if(int(l[0]) == 12 ) else ":".join( l )
    else:
        return ":".join(l) if( int(l[0]) == 12 ) else ":".join([str(int( l[0] ) + 12)] + l[1:])

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)

    print( result )
