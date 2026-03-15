t = int(input())
for i in range(t):
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr1.sort()
    m = int(input())
    arr2 = list(map(int,input().split()))

    for j in range(m):
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if arr1[mid] > arr2[j]:
                right = mid - 1
            elif arr1[mid] < arr2[j]:
                left = mid + 1
            else:
                print(1)
                break
        else:
            print(0)

# t * (n + m) * log n