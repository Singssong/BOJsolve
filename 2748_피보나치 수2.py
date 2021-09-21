import sys
input = sys.stdin.readline

n = int(input())
a = 0
b = 1
for i in range(1,n):
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    else:
        c = a + b
        a = b
        b = c

print(c)