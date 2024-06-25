def move_line(n, numbers):
    d = [1] * (n + 1)
    num = [0] + numbers

    for i in range(1, n+1):
        for j in range(1, i):
            if num[j] < num[i]:
                d[i] = max(d[i], d[j] + 1)

    return n - max(d)

n = int(input())
numbers = [int(input()) for _ in range(n)] 

print(move_line(n, numbers))