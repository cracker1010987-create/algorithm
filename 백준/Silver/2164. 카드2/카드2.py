from collections import deque

n = int(input())

arr = deque(range(1, n + 1))
for _ in range(n - 1):
    arr.popleft()
    arr.rotate(-1)
print(arr[0])