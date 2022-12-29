"""
문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
"""

from sys import stdin

# 입력
N, M = map(int, stdin.readline().split())
numList = list(map(int, stdin.readline().split()))
numList.sort()

# 과정
def recursive(num):
  if (M == num):
    res.add(tuple(result))
    return
  
  for i in range(N):
    result.append(numList[i])
    recursive(num+1)
    result.pop()
    

result = []
res = set()

# 출력
recursive(0)
for item in sorted(res):
  print(*item)