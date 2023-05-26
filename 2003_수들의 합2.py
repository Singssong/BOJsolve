"""
문제
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

출력
첫째 줄에 경우의 수를 출력한다.
"""

from sys import stdin

cnt = 0

N, M = map(int, stdin.readline().rstrip().split(" "))
A = list(map(int, stdin.readline().rstrip().split(" ")))

l = 0
r = 1
total = A[l]
while(r <= N and l <= r):
  total = sum(A[l:r])
  if total == M:
    cnt += 1
    l += 1
  elif total < M:
    r += 1
  else:
    l += 1
if (total == M):
  cnt +=1

print(cnt)
