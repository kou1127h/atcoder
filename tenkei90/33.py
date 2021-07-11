import math
H, W = list(map(int, input().split()))
ans = 0
if H == 1 or W == 1:
    ans = H * W
else:
    row = math.ceil(W/2)
    col = math.ceil(H/2)
    ans = row * col
print(ans)
