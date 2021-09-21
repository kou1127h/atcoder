N = int(input())
S = input()

count = 0
ans = 0

for n in S:
    if n == "A":
        count = 1
    elif count == 1 and n == "B":
        count += 1
    elif count == 2 and n == "C":
        ans += 1
        count = 0
    else:
        count = 0


print(ans)
