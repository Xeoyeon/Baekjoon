import sys
T= int(sys.stdin.readline().rstrip())
Q=25
D=10
N=5
P=1
for i in range(T):
    money= int( sys.stdin.readline().rstrip())
    money_Q=money//Q
    money=money%Q #헷갈리면 중간 저장 변수를 사용하자자
    money_D=money//D
    money=money%D
    money_N=money//N
    money=money%N
    money_P=money//P
    print(money_Q,money_D,money_N,money_P)
    