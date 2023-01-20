"""
문제
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.
"""

from sys import stdin
from collections import deque
# 오 -> 아 -> 왼 -> 위 -> 위오 -> 아래오 -> 아래왼 -> 위왼 (8)
dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, -1, 1, 1, -1]


while 1:
  def bfs(y, x):
    q = deque()
    q.append((y, x))
    while q:
      py, px = q.popleft()
      for k in range(8):
        nx = px + dx[k]
        ny = py + dy[k]
        if 0 <= nx < w and 0 <= ny < h:
          if visited[ny][nx] == False and graph[ny][nx] == 1:
            visited[ny][nx] = True
            q.append((ny, nx))
            
  w, h = map(int, stdin.readline().rstrip().split())
  cnt = 0
  visited = [[False for _ in range(w)] for _ in range(h)]
  if w == 0 and h == 0:
    exit(0)
  
  graph = [[] for _ in range(h)]
  for i in range(h):
    graph[i] = list(map(int, stdin.readline().rstrip().split()))
  
  for y in range(h):
    for x in range(w):
      if visited[y][x] == False and graph[y][x] == 1:
        visited[y][x] = True
        cnt += 1
        bfs(y, x)
  
  print(cnt)
  