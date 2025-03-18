import sys
N = int(sys.stdin.readline().rstrip())
total_score=0
score_list= list(map(int, sys.stdin.readline().strip().split()))    
max_num=max(score_list)

for i in range(N):
    total_score += score_list[i]/max_num*100
        
print(total_score/N)