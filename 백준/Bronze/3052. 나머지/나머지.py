import sys
arr =[]
for i in range(10):
    num = int(sys.stdin.readline().rstrip())%42
    if num not in arr:
        arr.append(num)
        
print(len(arr))