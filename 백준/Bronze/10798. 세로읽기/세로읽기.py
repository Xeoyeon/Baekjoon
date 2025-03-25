import sys

A = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
max_len =0
for i in range(5):
    if len(A[i]) > max_len:
        max_len = len(A[i])
        
for i in range(5):
    if len(A[i]) < max_len:
        A[i] += ['10'] * (max_len - len(A[i]))
        
for i in range(max_len):        
    for j in range(5):
        if A[j][i] =='10':  # 10은 출력하지 않음
            continue
        print(A[j][i], end="")