N, X = list(map(int, input().split()))
a = list(map(int, input().split()))

pop_list = []
for index, item in enumerate(a):
    if item == X:
        pop_list.append(index)

for i in sorted(pop_list, reverse=True):
    a.pop(i)

print(*a)
