S = input()

ans = True
for i in range(len(S)):
    if i % 2 == 0 and S[i].isupper():
        ans = False
    elif i % 2 != 0 and S[i].islower():
        ans = False

print("Yes" if ans else "No")
