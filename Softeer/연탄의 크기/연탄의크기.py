def max_usable_houses(n, stove):
    max_houses = 0
    for radius in range(2, 101):
        count = sum(1 for r in stove if r % radius == 0)
        max_houses = max(max_houses, count)
    return max_houses

n = int(input())
stove = map(int, input().split())

print(max_usable_houses(n, stove))