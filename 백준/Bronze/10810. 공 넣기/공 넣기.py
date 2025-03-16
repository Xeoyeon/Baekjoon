import sys
bucket,count=map(int,sys.stdin.readline().strip().split())
bucket_list =[0]*bucket
for i in range(count):
    a,b,c = map(int, sys.stdin.readline().strip().split())
    for j in range(a,b+1):
        bucket_list[j-1]=c

for i in bucket_list:
    print(i,end=" ")