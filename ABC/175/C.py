X, K, D = list(map(int, input().split()))

if K == 1:
    print(min(abs(X+D), abs(X-D)))
else:
    ans = 0

    if X + D * K < 0:
        ans = abs(X + D * K)
    if X - D * K > 0:
        ans = abs(X - D * K)

    ok = X + K * D
    ng = X - K * D


# while
