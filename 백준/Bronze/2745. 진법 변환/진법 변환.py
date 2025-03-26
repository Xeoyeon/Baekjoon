import sys
N,B= sys.stdin.readline().split()
num_list="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
total=0
for i, value in enumerate(N[::-1]):
    total+=num_list.index(value)*(int(B)**i)
print(total)