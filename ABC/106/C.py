S = [int(i) for i in input()]
K = int(input())

streak = 0
ans = 0
for i in S:
    if i == 1:
        streak += 1
        if streak == K:
            ans = 1
            break
    else:
        streak = 0
        ans = i
        break
print(ans)
