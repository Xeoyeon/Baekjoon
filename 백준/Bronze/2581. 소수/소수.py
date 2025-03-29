import sys
M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
num_list=[] #소수를 저장할 리스트

def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

for num in range(M,N+1):
    if is_prime(num):
        num_list.append(num)

if len(num_list)>0:
    print(sum(num_list))
    print(min(num_list))
else:
    print(-1)