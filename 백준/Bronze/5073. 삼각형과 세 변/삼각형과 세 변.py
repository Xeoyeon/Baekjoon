import sys

while True:
    a,b,c= map(int, sys.stdin.readline().split())
    if a==b==c==0:
        break
    list=[a,b,c]
    max_len=max(list)
    list.remove(max_len)
    if max_len < sum(list):
        if a==b==c:
            print("Equilateral")
        elif a==b or b==c or a==c:
            print("Isosceles")
        elif a!=b and b!=c and c!=a:
            print("Scalene")
    else:
        print("Invalid")