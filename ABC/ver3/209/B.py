import math
N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

diff = math.floor(N / 2)
sum_a = sum(A)
if X >= sum_a - diff:
    print("Yes")
else:
    print("No")
