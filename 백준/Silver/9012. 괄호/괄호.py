n = int(input())
for i in range(n):
    vps = input().strip()
    count = 0
    for j in vps:
        if j == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            break
    if count == 0:
        print("YES")
    else:
        print("NO")