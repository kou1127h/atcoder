from math import floor
N = int(input())


ans = floor(1.08 * N)

if ans < 206:
    print("Yay!")
elif ans == 206:
    print("so-so")
else:
    print(":(")
