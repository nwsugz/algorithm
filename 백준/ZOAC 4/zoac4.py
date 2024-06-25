# def max_participants(W, H, N, M):
#     cols = (W + M) // (M + 1)
#     rows = (H + N) // (N + 1)
    
#     return cols * rows

# W, H, N, M = map(int, input().strip().split())

# result = max_participants(W, H, N, M)

# print(result)

import math
H, W, N, M = map(int, input().split())
a = math.ceil(W/(M+1))
b = math.ceil(H/(N+1))
print(a*b)