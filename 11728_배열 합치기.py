"""
문제
정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000,000)

둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용이 주어진다. 배열에 들어있는 수는 절댓값이 109보다 작거나 같은 정수이다.

출력
첫째 줄에 두 배열을 합친 후 정렬한 결과를 출력한다.
"""

from sys import stdin

# 배열 A의 크기 N, 배열 B의 크기 M
N, M = map(int, stdin.readline().rstrip().split(" "))

A = list(map(int, stdin.readline().rstrip().split(" ")))
B = list(map(int, stdin.readline().rstrip().split(" ")))

# A의 포인터 up, B의 포인터 down
up = 0
down = 0

# 정답 배열 answer
answer = []

while(1):
  if up == N:
    for i in range(down, M):
      answer.append(B[i])
    break
  elif down == M:
    for i in range(up, N):
      answer.append(A[i])
    break
  elif A[up] >= B[down]:
    answer.append(B[down])
    down += 1
  elif A[up] < B[down]:
    answer.append(A[up])
    up += 1

for item in answer:
  print(item, end=" ")