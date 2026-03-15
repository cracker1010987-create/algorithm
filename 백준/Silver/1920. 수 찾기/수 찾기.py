n = int(input())
arr1 = list(map(int,input().split()))
arr1.sort()
m = int(input())
arr2 = list(map(int,input().split()))
for i in range(m):
    curr = arr2[i]

    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2

        if arr1[mid] > curr:
            right = mid - 1
        elif arr1[mid] < curr:
            left = mid + 1
        else:
            print(1)
            break

    else:
        print(0)
