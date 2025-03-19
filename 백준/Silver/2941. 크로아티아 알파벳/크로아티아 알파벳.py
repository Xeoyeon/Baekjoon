import sys
words =["c=","c-","dz=","d-","lj","nj","s=","z="]
input= sys.stdin.readline().rstrip()
for i in words:
    input = input.replace(i,"*")
print(len(input))