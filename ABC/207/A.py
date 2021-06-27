array = list(map(int, input().split()))

sort_array = sorted(array, reverse=True)
print(sort_array[0] + sort_array[1])
