import sys
T = sys.stdin.readline().rstrip()
for _ in range(int(T)):
    R, S = sys.stdin.readline().rstrip().split()
    for i in S:
        print(i*int(R), end="")
    print()