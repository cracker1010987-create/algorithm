t = int(input())
for _ in range(t):
    string = input()
    ans = ""
    ans += string[0] + string[-1]
    print(ans)