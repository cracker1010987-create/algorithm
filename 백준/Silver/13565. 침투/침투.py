from collections import deque
import sys
input = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

m, n = map(int, input().split())
grid = [list(map(int, list(input().strip()))) for _ in range(m)]

q = deque([])
for j in range(n):
    if grid[0][j] == 0:
        q.append((0, j))
        grid[0][j] = 2

ans = "NO"
while q:
    curr_y, curr_x = q.popleft()
    if curr_y == m - 1:
        ans = "YES"
        break

    for i in range(4):
        ny, nx = curr_y + dy[i], curr_x + dx[i]
        if 0 <= ny < m and 0 <= nx < n and grid[ny][nx] == 0:
            q.append((ny, nx))
            grid[ny][nx] = 2

print(ans)