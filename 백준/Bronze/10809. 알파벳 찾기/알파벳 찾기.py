import sys
import string
word = sys.stdin.readline().rstrip()
for char in string.ascii_lowercase:
    print(word.find(char), end=" ")