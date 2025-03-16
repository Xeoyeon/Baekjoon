import sys
num_list=[]
not_list=[]
for i in range(28):
    num_list.append(int(sys.stdin.readline().rstrip()))
for i in range(1,31):
    if i not in num_list:
        not_list.append(i)
not_list.sort()
for i in not_list:
    print(i)