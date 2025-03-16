import sys
T =sys.stdin.readline().rstrip()
nums = list(map(int, sys.stdin.readline().split()))
print(min(nums), max(nums))