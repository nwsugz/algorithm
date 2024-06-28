def indirect_indexing(n, pairs):
    result = []
    for Si, Ti in pairs:
        Pi = Si.lower().index('x')
        result.append(Ti[Pi].upper())
    return ''.join(result)

n = int(input())
pairs = [input().split() for i in range(n)]

print(indirect_indexing(n, pairs))