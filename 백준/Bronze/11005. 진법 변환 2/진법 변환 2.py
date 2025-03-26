import sys
N,B=map(int,sys.stdin.readline().split())
num_list="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number_B=""
number_10=N
while True :
    if number_10<B:
        number_B+=num_list[number_10]
        break
    나머지=number_10%B 
    number_B+=num_list[나머지]
    number_10=number_10//B #여기서 정수로 나누어야 함. 그래야 아래의 % 나머지 연산에서도 정수로 출력
print(number_B[::-1])