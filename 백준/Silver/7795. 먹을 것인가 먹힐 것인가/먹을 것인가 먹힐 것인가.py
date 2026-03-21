test = int(input())
for _ in range(test):
    n, m = map(int, input().split())
    arr1 = (list(map(int, input().split())))
    arr2 = (list(map(int, input().split())))
    arr1.sort()
    arr2.sort()
    cnt = 0
    b_i = 0
    for i in range(n):
        while b_i < m and arr1[i] > arr2[b_i]:
            b_i += 1

        cnt += b_i
    print(cnt)