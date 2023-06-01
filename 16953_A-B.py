"""
문제
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다. 
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

입력
첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

출력
A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.
"""

from sys import stdin
from collections import deque

def bfs(num, cnt):
  global answer
  q = deque()
  q.append((num, cnt))

  while(q):
    pop_num, pop_cnt = q.popleft()

    if (pop_num == B):
      answer = min(answer, pop_cnt)
    elif pop_num > B:
      continue
    else:
      q.append((pop_num * 2, pop_cnt + 1))
      q.append((pop_num * 10 + 1, pop_cnt + 1))



# A: start, B: target
A, B = map(int, stdin.readline().rstrip().split(" "))
answer = 10000000000
bfs(A, 0)

if (answer == 10000000000):
  print(-1)
else:
  print(answer + 1)