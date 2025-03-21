import sys
T = sys.stdin.readline().rstrip()
count =0
for _ in range(int(T)):
    group =[]
    is_group_word = True
    prev_char=''
    word = sys.stdin.readline().rstrip()
    for char in word:
        if char!=prev_char and char in group:
            is_group_word = False
            break
        else:
            group.append(char)
        prev_char =char
    if(is_group_word):
        count+=1
print(count)