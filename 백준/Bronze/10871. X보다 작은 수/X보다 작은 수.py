import sys
a,b = map(int, sys.stdin.readline().strip().split())
A = map(int, sys.stdin.readline().strip().split())
arr=""
for i in A:
    if i<b:
        arr=arr+str(i)+" "
print(arr)