import sys
a,b = map(int, sys.stdin.readline().strip().split())
A = map(int, sys.stdin.readline().strip().split())
for i in A:
    if i<b:
        print(i,end=" ")
