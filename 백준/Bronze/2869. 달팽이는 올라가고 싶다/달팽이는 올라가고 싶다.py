import sys
A,B,V=map(int, sys.stdin.readline().rstrip().split())
day = (V-B)//(A-B)
if (V-B)%(A-B)==0:
    print(day)
else:
    print(day+1)