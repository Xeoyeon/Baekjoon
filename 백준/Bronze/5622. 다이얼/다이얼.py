import sys
text_list = list(sys.stdin.readline().rstrip())
alp_list=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ",""]
sum =0 
for text in text_list:
    for alpha in alp_list:
        if text in alpha:
           sum += alp_list.index(alpha)+3
print(sum)