#순열
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
num_arr = list(map(int, input().split()))
numOfOp = list(map(int, input().split()))
sortOfOp = ['+', '-', '*', '/']
op_arr = []
for i in range(len(numOfOp)):
    for j in range(numOfOp[i]):
        op_arr.append(sortOfOp[i])

maximun = -1e9
minimun = 1e9

def calc():
    global maximun, minimun
    for case in list(permutations(op_arr, n-1)):
        res = num_arr[0]
        for i in range(n-1):
            if case[i] == '+':
                res += num_arr[i+1]
            elif case[i] == '-':
                res -= num_arr[i+1]
            elif case[i] == '*':
                res *= num_arr[i+1]
            elif case[i] == '/':
                if res < 0:
                    res = -res
                    res = res // num_arr[i+1]
                    res = -res
                else:
                    res = res // num_arr[i+1]
        if res > maximun:
            maximun = res
        if res < minimun:
            minimun = res
calc()
print(maximun)
print(minimun)