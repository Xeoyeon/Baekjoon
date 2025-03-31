import sys
n=int(sys.stdin.readline().rstrip())
sum=0
for i in range(1,n-1):
    sum += i*(n-i-1)
print(sum)
print(3)
