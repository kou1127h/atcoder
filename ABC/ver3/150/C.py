import itertools

N = int(input())

p = list(map(int, input().split()))
q = list(map(int, input().split()))

index_p = -1
index_q = -1
i = 0
for v in itertools.permutations(range(1, N + 1), N):
    i += 1
    item = list(v)
    # print(item, p, q)
    if p == item:
        index_p = i
    if q == item:
        index_q = i
    if index_p != -1 and index_q != -1:
        break

print(abs(index_p - index_q))
