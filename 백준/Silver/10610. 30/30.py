arr = list(map(int,input()))

if sum(arr) % 3 == 0 and 0 in arr:
    arr.sort(reverse=True)
    arr = list(map(str, arr))
    print("".join(arr))
else:
    print(-1)