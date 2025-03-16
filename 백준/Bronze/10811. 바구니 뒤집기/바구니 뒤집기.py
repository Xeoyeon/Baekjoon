import sys
new_arr=[]
basket, cnt = map(int,sys.stdin.readline().rstrip().split())
arr=[i+1 for i in range(basket)]
for _ in range(cnt):
    a,b =map(int,sys.stdin.readline().strip().split())
    arr[a-1:b] = arr[a-1:b][::-1]
for i in arr:
    print(i,end=" ")