import sys
type=""
while True:
    a,b=map(int,sys.stdin.readline().rstrip().split())
    if a==0 or b==0:
        break
    
    if b%a==0:
        type="factor"
    elif a%b==0:
        type="multiple"
    else:
        type="neither"
    print(type)