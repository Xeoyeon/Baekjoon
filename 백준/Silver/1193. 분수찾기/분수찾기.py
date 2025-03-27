import sys
X=int(sys.stdin.readline().rstrip())

num=0
count =0

while X>num:
    count+=1
    num+=count
    
loc= X-(num-count)#while문에서 count가 한번 더 더해진거니까 빼줘야 함.

if count%2==0: #짝수이면
    print(f"{loc}/{count + 1 - loc}")#합이 count+!
else:
    print(f"{count + 1 - loc}/{loc}")