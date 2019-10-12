#!/bin/python3
#https://www.hackerrank.com/contests/projecteuler/challenges/euler2/problem
import sys
import os
def fib_sum(arr):
    result = []
    for nterms in arr:
        #fibonacci series generator
        z =[1, 2];
        s =2
        while(z[-1]+z[-2]<=nterms):
            z.append(z[-2]+z[-1])
            if(z[-1]%2 == 0):
            #end of generation
                s+=z[-1] # the sum of the elements in the series
        result.append(s)
    return "\n".join([str(x) for x in result])
stdin = open(os.environ['OUTPUT_PATH'], 'w')
arr = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr.append(n)
result = fib_sum(arr)
stdin.write(result)
stdin.close()

