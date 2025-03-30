import sys
a,b,c= map(int, sys.stdin.readline().split())

while True:
    max_len=max(a,b,c)
    sum_len=a+b+c
    if max_len < sum_len-max_len:
        break
    if a==max_len:
        a-=1
    elif b==max_len:
        b-=1
    elif c==max_len:
        c-=1
print(sum_len)