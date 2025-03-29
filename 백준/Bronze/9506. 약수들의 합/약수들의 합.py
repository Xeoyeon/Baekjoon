import sys

while True:

    divisor=[]
    sum=0
    sum_output=""
    
    num=int(sys.stdin.readline().rstrip())
    
    if num ==-1:
        break
    
    for i in range(1, num-1):
        if num%i==0:
            divisor.append(i)
    for k in divisor:
        sum+=k
        
    if sum==num:
        print(f"{num} = "+" + ".join(map(str,divisor)))        
    else:
        print(f"{num} is NOT perfect.")