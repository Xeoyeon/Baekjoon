import sys
count=0
N = int(sys.stdin.readline().rstrip())
num= list(map(int,sys.stdin.readline().rstrip().split()))
for i in num:
    divisor=[]
    for k in range(1,i+1):
        if i%k==0:
            divisor.append(k)
        
    if len(divisor)==2:
        count+=1
    
print(count)    