import sys
num=int(sys.stdin.readline().rstrip())
count=1
max_num=1

while num > max_num:
    max_num+=6*count #덧셈이 뺄셈보다 연산 효율 좋음
    count+=1
    
print(count)