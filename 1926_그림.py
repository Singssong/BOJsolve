"""
문제
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

입력
첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

출력
첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
"""

# BFS

from sys import stdin
from collections import deque

# 오 -> 아 -> 왼 -> 위
dy = [0,1,0,-1] 
dx = [1,0,-1,0]

def bfs(y, x):
  queue = deque()
  queue.append((y, x))
  width = 1
  while queue:
    ey, ex = queue.pop()
    for k in range(4):
      ny = ey + dy[k]
      nx = ex + dx[k]
      if 0 <=ny<N and 0<=nx<M:
        if l[ny][nx] == "1" and visited[ny][nx] == False:
          width += 1
          visited[ny][nx] = True
          queue.append((ny, nx))
  return width

N, M = map(int, stdin.readline().rstrip().split())
visited = [[False for _ in range(M)] for _ in range(N)]
l = []
cnt = 0
maxValue = 0

for i in range(N):
  l.append(stdin.readline().rstrip().split())

for y in range(N):
  for x in range(M):
    if l[y][x] == "1" and visited[y][x] == False:
      visited[y][x] = True
      cnt += 1
      maxValue = max(maxValue, bfs(y, x))

print(cnt)
print(maxValue)