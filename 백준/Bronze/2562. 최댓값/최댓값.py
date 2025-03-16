import sys
nums=[]
for _ in range(9):
    T =sys.stdin.readline().rstrip()
    nums.append(int(T))

print(max(nums))
print(nums.index(max(nums))+1)
