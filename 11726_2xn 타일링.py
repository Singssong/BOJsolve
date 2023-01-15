"""
문제
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.



입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
"""

from sys import stdin

res = [0 for _ in range(1002)]
res[1] = 1
res[2] = 2
res[3] = 3
n = int(stdin.readline())

if n > 2:
  for i in range(3, n+2):
    if (i==n+1):
      print(res[n] % 10007)
    res[i] = res[i-2] + res[i-1]
else:
  print(res[n] % 10007)
