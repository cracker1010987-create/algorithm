from collections import deque

n = int(input())
person1, person2 = map(int, input().split())
m = int(input())
relations = [list(map(int, input().split())) for _ in range(m)]

relation_list = [[] for _ in range(n + 1)]
for x, y in relations:
    relation_list[x].append(y)
    relation_list[y].append(x)

visited = [False] * (n + 1)

q = deque([(person1, 0)])
visited[person1] = True
ans = -1
while q:
    curr_person, curr_num = q.popleft()
    flag = False
    for child in relation_list[curr_person]:
        if child == person2:
            ans = curr_num + 1
            flag = True
        elif not visited[child]:
            visited[child] = True
            q.append((child, curr_num + 1))
    if flag:
        break

print(ans)