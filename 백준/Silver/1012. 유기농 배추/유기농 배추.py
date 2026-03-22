import sys
input = sys.stdin.readline

t = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for _ in range(t):
    m, n, k = map(int,input().split())
    points = [list(map(int,input().split())) for _ in range(k)]
    farm = [[0] * n for _ in range(m)]

    cnt = 0
    for x,y in points:
        farm[x][y] = 1
    for x,y in points:
        if farm[x][y] == 1:
            farm[x][y] = 2
            stack = [[x,y]]
            cnt += 1
            while stack:
                cx, cy = stack.pop()
                for i in range(4):
                    nx, ny = cx + dx[i],cy + dy[i]
                    if 0 <= nx < m and 0 <= ny < n and farm[nx][ny] == 1:
                        farm[nx][ny] = 2
                        stack.append([nx, ny])
    print(cnt)

