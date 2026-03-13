n = int(input())
ans = int(input())
num = list(map(int,input().split()))
num.sort()

l = 0
r = n - 1
cnt = 0
while l < r:
    if num[r] + num[l] < ans:
        l += 1
    elif num[r] + num[l] > ans:
        r -= 1
    else:
        l += 1
        r -= 1
        cnt += 1
print(cnt)