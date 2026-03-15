import sys
input = sys.stdin.readline


n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]

nums.sort()

st = 0
en = 1
ans = float('inf')
while en < n:
    diff = nums[en] - nums[st]
    if diff < m:
        en += 1
    elif diff > m:
        if diff < ans:
            ans = diff
        st += 1
    else:
        print(m)
        break
else:
    print(ans)