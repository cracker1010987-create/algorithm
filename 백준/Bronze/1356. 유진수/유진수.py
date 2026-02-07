n = input()
for i in range(1, len(n)):
    left = n[:i]
    right = n[i:]
    left_ans = 1
    right_ans = 1
    for j in range(len(left)):
        left_ans *= int(left[j])
    for k in range(len(right)):
        right_ans *= int(right[k])
    if right_ans == left_ans:
        print("YES")
        break
else:
    print("NO")
    
