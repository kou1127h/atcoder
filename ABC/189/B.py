N, X = list(map(int, input().split()))

alc = 100 * X
cap = 0
index = 0
for i in range(N):
    v, p = list(map(int, input().split()))
    cap += v * p
    index += 1
    if cap > alc:
        print(index)
        break

if cap <= alc:
    print(-1)
