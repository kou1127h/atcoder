N = int(input())
S = [i for i in input()]
Q = int(input())

reversed = -1
ans = ""
for i in range(Q):
    t, a, b = map(int, input().split())
    if t == 2:
        reversed *= -1
    else:
        a -= 1
        b -= 1
        if reversed == 1:
            if a >= N:
                a = a - N
            else:
                a = a + N
            if b >= N:
                b = b - N
            else:
                b = b + N
        S[a], S[b] = S[b], S[a]
if reversed == 1:
    ans = ''.join(S[N:]) + ''.join(S[:N])
else:
    ans = ''.join(S)
print(ans)
