from collections import deque
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def solution(maps):
    start = [0, 0, 1]
    goal_x, goal_y = len(maps) - 1, len(maps[0]) - 1
    q = deque([])
    q.append(start)
    maps[0][0] = 2
    
    while q:
        curr_x, curr_y, curr_d = q.popleft()
        if curr_x == goal_x and curr_y == goal_y:
            return curr_d
            
        for i in range(4):
            next_x, next_y = curr_x + dx[i], curr_y + dy[i]
            if 0 <= next_x <= goal_x and 0 <= next_y <= goal_y:
                if maps[next_x][next_y] == 1:
                    q.append([next_x, next_y, curr_d + 1])
                    maps[next_x][next_y] = 2
    else:
        return -1
   