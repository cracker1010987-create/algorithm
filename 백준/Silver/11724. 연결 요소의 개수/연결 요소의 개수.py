from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
visited = [False] * (n + 1)
count = 0

for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        q = deque([i])
        visited[i] = True

        while q:
            curr = q.popleft()

            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
print(count)