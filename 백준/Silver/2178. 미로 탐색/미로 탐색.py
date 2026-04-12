from collections import deque
import sys

input = sys.stdin.readline
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
q = deque([])
q.append([0, 0, 1])
arr[0][0] = 2  # 2는 방문한 노드 표시
while q:
    curr_x, curr_y, curr_d = q.popleft()
    if curr_x == m - 1 and curr_y == n - 1:
        print(curr_d)
        break

    for i in range(4):
        nx = curr_x + dx[i]
        ny = curr_y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 1:
            q.append([nx, ny, curr_d + 1])
            arr[ny][nx] = 2
