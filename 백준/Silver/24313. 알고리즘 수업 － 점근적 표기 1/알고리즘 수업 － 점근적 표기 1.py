import sys

a,b= map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

if a <= c and b <= (c - a) * n:
    print(1)
else:
    print(0)