import sys
a,b =sys.stdin.readline().rstrip().split()
rev_a = int(a[::-1])
rev_b = int(b[::-1])
print(max(rev_a,rev_b))