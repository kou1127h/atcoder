N = input()

added = 0
for n in N:
    added += int(n)

print("Yes" if added % 9 == 0 else "No")
