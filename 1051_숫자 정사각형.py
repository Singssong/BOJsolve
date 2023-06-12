"""
숫자 정사각형
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	18461	7826	6653	43.243%
문제
N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다. 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오. 이때, 정사각형은 행 또는 열에 평행해야 한다.

입력
첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 수가 주어진다.

출력
첫째 줄에 정답 정사각형의 크기를 출력한다.
"""

from sys import stdin

N, M = map(int, stdin.readline().rstrip().split(" "))

graph = []
max_length = min(N,M)
answer = 1

for i in range(N):
  line = stdin.readline().rstrip()
  temp = []
  for j in range(len(line)):
    temp.append(line[j])
  graph.append(temp)


for y in range(N):
  for x in range(M):
    for length in range(1, max_length):
      if (x+length < M and y+length < N):
        if (graph[y][x] == graph[y][x+length] == graph[y+length][x] == graph[y+length][x+length]):
          answer = max(answer, (length+1) * (length+1))

print(answer)