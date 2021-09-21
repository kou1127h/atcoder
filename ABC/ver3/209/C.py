import sys
input = sys.stdin.readline

mod = 10 ** 9 + 7
N = int(input())
C = list(map(lambda k: int(k) % mod, input().split()))


C.sort()
ans = 1
for i, c in enumerate(C):
    ans *= (c - i)
    ans = ans % mod

print(ans)
