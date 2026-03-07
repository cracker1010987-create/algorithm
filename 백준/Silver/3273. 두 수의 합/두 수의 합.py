n = int(input())
arr = list(map(int,input().split()))
ans = int(input())

arr.sort()
l, r = 0, n - 1
cnt = 0
while l < r:
    curr = arr[l] + arr[r]
    if curr < ans:
        l += 1
    elif curr > ans:
        r -= 1
    else:
        cnt += 1
        l += 1
        r -= 1
print(cnt)
