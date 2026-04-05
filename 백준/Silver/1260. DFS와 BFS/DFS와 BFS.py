from collections import deque
import sys

input = sys.stdin.readline
n, m, v = map(int,input().split())
relation_list = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int,input().split())
    relation_list[a].append(b)
    relation_list[b].append(a)

for i in range(1, n + 1):
    relation_list[i].sort()

bfs_list = deque([v])
bfs_ans = []
visited = [False for _ in range(n + 1)]
while bfs_list:
    curr_node = bfs_list.popleft()
    if not visited[curr_node]:
        visited[curr_node] = True
        bfs_ans.append(curr_node)
        next_nodes = relation_list[curr_node]
        for node in next_nodes:
            if not visited[node]:
                bfs_list.append(node)

for i in range(1, n + 1):
    relation_list[i].sort(reverse=True)

dfs_list = [v]
visited = [False for _ in range(n + 1)]
dfs_ans = []
while dfs_list:
    curr_node = dfs_list.pop()
    if not visited[curr_node]:
        visited[curr_node] = True
        dfs_ans.append(curr_node)
        next_nodes = relation_list[curr_node]
        for node in next_nodes:
            if not visited[node]:
                dfs_list.append(node)
print(*dfs_ans)
print(*bfs_ans)