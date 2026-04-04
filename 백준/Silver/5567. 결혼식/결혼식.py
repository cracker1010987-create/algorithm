from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
relation_list = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    relation_list[x].append(y)
    relation_list[y].append(x)
visited = [False] * (n + 1)
q = deque([(1, 0)])
visited[1] = True
invite_count = 0

while q:
    curr_person, dist = q.popleft()
    if dist < 2:
        for neighbor in relation_list[curr_person]:
            if not visited[neighbor]:
                visited[neighbor] = True
                invite_count += 1
                q.append((neighbor, dist + 1))

print(invite_count)