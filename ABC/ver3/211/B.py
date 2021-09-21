S = []
flag = True
for i in range(4):
    item = input()
    if item not in S:
        S.append(item)
    else:
        flag = False

print("Yes" if flag else "No")
