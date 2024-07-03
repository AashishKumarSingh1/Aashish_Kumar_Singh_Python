from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
fibonacci_series=[]
def setfibonacci(num):
    if num==1 or num==2:
        return 1
    fibonacci_series.append(fibonacci_series[num-1]+fibonacci_series[num-2])
    return 'done'
num=int(input())
setfibonacci(num)
print(fibonacci_series[num])