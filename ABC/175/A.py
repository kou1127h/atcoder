S = input()

streak = 0
ans = 0
for i in S:
    if i == "R":
        streak += 1
        ans = streak
    elif i == "S" and streak != 0:
        ans = streak
        streak = 0
print(ans)
