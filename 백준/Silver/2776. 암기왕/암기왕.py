t = int(input())
for i in range(t):
    n = int(input())
    arr1 = set(map(int,input().split()))
    m = int(input())
    arr2 = list(map(int,input().split()))

    for j in range(m):
        if arr2[j] in arr1:
            print(1)
        else:
            print(0)

# t * m