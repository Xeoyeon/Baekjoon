import sys
T=sys.stdin.readline().rstrip()
num_arr = map(int, sys.stdin.readline().split())
v = int(sys.stdin.readline().rstrip())
count=0
for i in num_arr:
    if i==v:
        count+=1
print(count)