from collections import deque
import sys

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

q = deque([])
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            q.append((i, j, 0))

ans_day = 0

while q:
    curr_y, curr_x, curr_day = q.popleft()
    ans_day = curr_day

    for i in range(4):
        ny, nx = curr_y + dy[i], curr_x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == 0:
            grid[ny][nx] = 1
            q.append((ny, nx, curr_day + 1))

for row in grid:
    if 0 in row:
        print(-1)
        break
else:
    print(ans_day)