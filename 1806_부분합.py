"""
문제
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

출력
첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.
"""

from sys import stdin

N, S = map(int, stdin.readline().rstrip().split(" "))
A = list(map(int, stdin.readline().rstrip().split(" ")))

l = 0
r = 0
total = 0
answer = 10000000
while (1):
  if total >= S:
    answer = min(answer, r - l)
    total -= A[l]
    l += 1
  elif r == N:
    break
  else:
    total += A[r]
    r += 1

if answer == 10000000:
  print(0)
else:
  print(answer)