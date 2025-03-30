import sys

x,y,w,h= map(int,sys.stdin.readline().rstrip().split())

len=[x,y,abs(w-x),abs(h-y)]

print(min(len))