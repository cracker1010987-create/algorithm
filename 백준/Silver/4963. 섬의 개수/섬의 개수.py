from collections import deque
import sys

input = sys.stdin.readline
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    grid = [list(map(int, input().split())) for _ in range(h)]
    island_count = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                island_count += 1
                q = deque([(i, j)])
                grid[i][j] = 0 

                while q:
                    curr_y, curr_x = q.popleft()

                    for k in range(8):
                        ny, nx = curr_y + dy[k], curr_x + dx[k]
                        if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == 1:
                            grid[ny][nx] = 0 
                            q.append((ny, nx))

    print(island_count)