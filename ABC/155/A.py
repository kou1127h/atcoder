a, b, c = list(map(int, input().split()))
if (a == b and a != c) or (a == c and a != b) or (c == b and a != c):
    print("Yes")
else:
    print("No")
