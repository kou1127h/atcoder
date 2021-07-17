X, K, D = list(map(int, input().split()))

if X < 0:
    X = -X

A = X % D
B = X // D
ans = 0
if B >= K:
    ans = X - D * K
else:
    if (K - B) % 2 == 0:
        ans = A
    else:
        ans = abs(A - D)
print(ans)
