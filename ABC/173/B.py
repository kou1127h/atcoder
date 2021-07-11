N = int(input())

ac = 0
wa = 0
tle = 0
re = 0

for i in range(N):
    S = input()
    if S == "AC":
        ac += 1
    if S == "WA":
        wa += 1
    if S == "TLE":
        tle += 1
    if S == "RE":
        re += 1

print(f"AC x {ac}")
print(f"WA x {wa}")
print(f"TLE x {tle}")
print(f"RE x {re}")
