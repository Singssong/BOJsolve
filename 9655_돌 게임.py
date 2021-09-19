import sys
input = sys.stdin.readline

N = int(input())
x = N % 6
if x == 0 or x == 2 or x == 4:
    print('CY')
else:
    print('SK')