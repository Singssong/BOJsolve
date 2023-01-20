"""
문제
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

"""

from sys import stdin
from collections import deque

# 오 아 왼 위
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


N = int(stdin.readline())

graph = [[] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
color = ["R", "G", "B"]

for i in range(N):
  graph[i] = list(stdin.readline().rstrip())



def bfs(y, x, color, type):
  q = deque()
  q.append((y, x))
  while q:
    py, px = q.popleft()
    for k in range(4):
      nx = px + dx[k]
      ny = py + dy[k]
      if 0 <= nx < N and 0 <= ny < N:
        if type == 0:
          if visited[ny][nx] == False and graph[ny][nx] == color:
            visited[ny][nx] = True
            q.append((ny, nx))
        elif (type == 1):
          if visited[ny][nx] == False and (graph[ny][nx] == "R" or graph[ny][nx] == "G"):
            visited[ny][nx] = True
            q.append((ny, nx))
        else:
          if visited[ny][nx] == False and graph[ny][nx] == "B":
            visited[ny][nx] = True
            q.append((ny, nx))
# 색약 X          
cnt = 0
for z in range(3):
  for y in range(N):
    for x in range(N):
      if visited[y][x] == False and graph[y][x] == color[z]:
        visited[y][x] = True
        cnt += 1
        bfs(y, x, color[z], 0)

# 색약 O
visited = [[False for _ in range(N)] for _ in range(N)]
cnt_weak = 0
for y in range(N):
  for x in range(N):
    if visited[y][x] == False and (graph[y][x] == "R" or graph[y][x] == "G"):
      visited[y][x] = True
      cnt_weak += 1
      bfs(y, x, color[z], 1)

for y in range(N):
  for x in range(N):
    if visited[y][x] == False and graph[y][x] == "B":
      visited[y][x] = True
      cnt_weak += 1
      bfs(y, x, color[z], 2)

print(cnt, cnt_weak)