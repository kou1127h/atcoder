N, K = list(map(int, input().split()))
h = list(map(int, input().split()))

cost = [0] * N

cost[0] = 0


cost[1] = cost[0] + abs(h[0] - h[1])

for i in range(2, N):
    temp = []
    for k in range(1, K+1):
        if i - k >= 0:
            temp.append(cost[i - k] + abs(h[i - k] - h[i]))
    cost[i] = min(temp)

print(cost[N-1])
