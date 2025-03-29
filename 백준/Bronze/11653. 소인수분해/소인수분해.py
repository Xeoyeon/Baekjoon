import sys
N= int(sys.stdin.readline().rstrip())
number=N
if N==2:
    print(2)
else:
    for i in range(2,int(N**0.5)+1):#N=2이면 범위가(2,2)여서 for문 실행이 안됨.예외 처리리
        while number%i==0: 
            number=number//i
            print(i)
    if number>1:
        print(number)        