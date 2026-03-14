n = int(input())
arr = list(map(int, input().split()))

prefix_sum = [0]
tmp = 0
for i in range(n):
    tmp += arr[i]
    prefix_sum.append(tmp)

ans = 0
for i in range(n - 1):
    ans += arr[i] * (prefix_sum[n] - prefix_sum[i+1])

print(ans)