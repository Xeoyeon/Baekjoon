import sys
num_list = list(map(int,sys.stdin.readline().split()))
chess_list = [1,1,2,2,2,8]
for i in range(6):
    print(chess_list[i]-num_list[i],end=" ")