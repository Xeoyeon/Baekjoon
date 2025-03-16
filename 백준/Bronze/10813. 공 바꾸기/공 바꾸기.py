import sys
T,cnt =map(int,sys.stdin.readline().rstrip().split())
num_list=[]
for i in range(T):
    num_list.append(i+1)

for i in range(cnt):
    a,b =map(int,sys.stdin.readline().strip().split())
    temp = num_list[a-1]
    num_list[a-1]=num_list[b-1]
    num_list[b-1]=temp

for i in num_list:
    print(i,end=" ")