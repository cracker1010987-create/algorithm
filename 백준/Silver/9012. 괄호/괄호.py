n = int(input())
for i in range(n):
    vps = input()
    arr = []
    for j in range(len(vps)):
        if vps[j] == "(":
            arr.append("(")
        else:
            if arr == []:
                print("NO")
                break
            else:
                arr.pop()
    else:
        if arr == []:
            print("YES")
        else:
            print("NO")