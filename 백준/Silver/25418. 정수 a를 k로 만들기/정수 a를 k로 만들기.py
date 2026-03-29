from collections import deque

n, m = map(int,input().split())
visited = set()
dist = 0
q = deque([(n, dist)])

while q:
    n, dist = q.popleft()
    next_num1 = n + 1
    next_num2 = n * 2

    if next_num2 == m or next_num1 == m:
        print(dist + 1)
        break

    if next_num1 not in visited and next_num1 < m:
        visited.add(next_num1)
        q.append((next_num1, dist + 1))

    if next_num2 not in visited and next_num2 < m:
        visited.add(next_num2)
        q.append((next_num2, dist + 1))

