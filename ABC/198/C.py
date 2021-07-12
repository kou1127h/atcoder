import math

R, X, Y = list(map(int, input().split()))
g_dist = pow(X ** 2 + Y ** 2, 0.5)
ans = 0
# 解説AC
# goalが円の中にある場合の考慮漏れ
if g_dist == R:
    ans = 1
elif g_dist != R and g_dist <= 2 * R:
    ans = 2
else:
    ans = math.ceil(g_dist / R)
print(ans)
