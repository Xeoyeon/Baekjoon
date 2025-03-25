import sys
N = int(sys.stdin.readline().rstrip())

array = [[0] * 100 for _ in range(100)]

for _ in range(N):  
    y1, x1 = map(int, input().split())  

    for i in range(x1, x1 + 10): # 도화지가 있는 좌표의 값을 1로 설정정
        for j in range(y1, y1 + 10):  
            array[i][j] = 1

result = 0  
for k in range(100):  # 전체 도화지를 돌면서 1을 세어 더해주면 전체 넓이가 됨됨
    result += array[k].count(1) 

print(result)
    