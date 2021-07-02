N = int(input())
A = list(map(int, input().split()))

ans = True
for n in range(N):
    if A[n] % 2 == 0 and (A[n] % 3 != 0 and A[n] % 5 != 0):
        ans = False
print("APPROVED" if ans else "DENIED")
