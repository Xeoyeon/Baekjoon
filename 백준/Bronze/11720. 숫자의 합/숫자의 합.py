import sys
count = int(sys.stdin.readline().rstrip())
numbers = sys.stdin.readline().rstrip()
total = 0 
for i in numbers:
    total += int(i)
print(total)