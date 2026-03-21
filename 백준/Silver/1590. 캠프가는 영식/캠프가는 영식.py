n, t = map(int, input().split())
ans = float('inf')

for _ in range(n):
    s, i, c = map(int, input().split())
    for k in range(c):
        bus_time = s + (i * k)
        if bus_time >= t:
            wait_time = bus_time - t
            if wait_time < ans:
                ans = wait_time
            break
if ans == float('inf'):
    print(-1)
else:
    print(ans)