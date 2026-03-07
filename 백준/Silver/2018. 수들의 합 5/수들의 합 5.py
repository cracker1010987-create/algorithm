n = int(input())

x = 1
sum_x = 1
cnt = 0
while n - sum_x >= 0:
    curr = n - sum_x
    if curr % x == 0:
        cnt += 1
    x += 1
    sum_x = x * (x + 1) // 2
print(cnt)