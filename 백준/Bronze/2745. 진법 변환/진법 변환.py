import sys
N,B= sys.stdin.readline().split()
my_dict ={
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 
    'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23,
    'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30,
    'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35
}
B=int(B)
num_list = list(N)
decimal= 0
for i in range(len(num_list)):
    if num_list[i].isdigit(): # isdigit()은 문자열이 숫자로만 이루어졌는지 판단하는 함수. 문자열에서만 적용됨됨
        decimal+= int(num_list[i])*(B**(len(num_list)-i-1))
    else:
        num = my_dict[num_list[i]] # 알파벳인 경우 dict에 대응되는 숫자로 변환후 계산
        decimal+= num*(B**(len(num_list)-i-1))
print(decimal)