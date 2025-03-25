import sys
N,M = map(int,sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

B = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = [[A[i][j] + B[i][j] for j in range(M)] for i in range(N)]

for row in result:
    print(*row) #'*'는 unpacking 연산자. 이를를 사용하면 리스트 안의 요소들을 공백으로 구분하여 출력할 수 있음음