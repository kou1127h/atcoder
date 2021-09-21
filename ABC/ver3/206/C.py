import collections

N = int(input())
A = list(map(int, input().split()))

count = (N * (N-1))/2
B = sorted(A)

c = collections.Counter(B)

for key in c.keys():
    if c[key] != 1:
        count -= (c[key] * (c[key]-1))/2

print(int(count))
