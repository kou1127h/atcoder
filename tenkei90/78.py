N, M = list(map(int, input().split()))
graph = []
for n in range(N):
    graph.append([])
for m in range(M):
    a, b = list(map(lambda k: int(k) - 1, input().split()))
    graph[a].append(b)
    graph[b].append(a)

ans = 0
for i in range(N):
    items = graph[i]
    count = 0
    for item in items:
        if i > item:
            count += 1
    if count == 1:
        ans += 1

print(ans)
