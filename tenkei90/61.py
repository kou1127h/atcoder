from collections import deque
Q = int(input())
deck = deque()

for q in range(Q):
    t, x = list(map(int, input().split()))
    if t == 1:
        deck.appendleft(x)
    elif t == 2:
        deck.append(x)
    elif t == 3:
        print(deck[x-1])
