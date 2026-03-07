n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0]
tmp = 0
cnt = 0
for i in range(n):
    tmp += arr[i]
    prefix_sum.append(tmp)
l, r = 0, 1
while r <= n:
    if prefix_sum[r] - prefix_sum[l] < m:
        r += 1
    elif prefix_sum[r] - prefix_sum[l] > m:
        l += 1
    else:
        cnt += 1
        r += 1
        l += 1
print(cnt)