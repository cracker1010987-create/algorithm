import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr1 =[int(input()) for _ in range(n)]

arr1.sort()

for _ in range(m):
    t = int(input())
    l = 0
    r = n - 1
    result = -1

    while l <= r:
        mid = (l + r) // 2

        if arr1[mid] == t:
            result = mid
            r = mid - 1
        elif arr1[mid] < t:
            l = mid + 1
        else:
            r = mid - 1

    print(result)