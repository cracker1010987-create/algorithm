check = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}
tmp_check = {chr(i): i - ord('A') + 27 for i in range(ord('A'), ord('Z') + 1)}
check.update(tmp_check)


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


arr = list(input())
total = 0
for i in arr:
    total += check[i]
if is_prime(total):
    print("It is a prime word.")
else:
    print("It is not a prime word.")
