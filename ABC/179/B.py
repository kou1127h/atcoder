N = int(input())

count = 0
ans = False
for i in range(N):
    a, b = list(map(int, input().split()))
    if a == b:
        count += 1
        if count == 3:
            ans = True
            break
    else:
        count = 0
print("Yes" if ans else "No")
