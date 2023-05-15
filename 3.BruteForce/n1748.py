import sys
input = sys.stdin.readline

def Answer(n):
    return(9 * pow(10, n-1) * n)

N = int(input())
length = len(str(N))

if length > 1:
    sum = (N - int('9' * (length - 1))) * length
    for i in range(1, length):
        sum += Answer(i)

else:
    sum = N

print(sum)

# n = input()
# k = 0
#
# for i in range(len(n)):
#     k += (int(n) - (10**i) + 1)
#     print(f'i={i}, k={k}')
#
# print(k)
