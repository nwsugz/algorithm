def count_votes(T, votes):
    results = []
    for n in votes:
        full_blocks = n // 5
        remainder = n % 5
        result = '++++ ' * full_blocks + '|' * remainder
        results.append(result)
    return results

T = int(input())
votes = [int(input()) for _ in range(T)]

results = count_votes(T, votes)
for result in results:
    print(result)