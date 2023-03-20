import sys

MAX = 1000000
li = [True] * (MAX + 1)
li[0] = False
li[1] = False

for i in range(2, int(MAX ** 0.5) + 1):
    if li[i]:
        for j in range(i * i, MAX, i):
            li[j] = False


def gold_bach(n):
    for i in range(0, n // 2 + 1):
        if li[i] and li[n - i]:
            print(f'{n} = {i} + {n - i}')
            return 0
    return 1


while True:
    n = int(sys.stdin.readline())

    if n == 0 or n % 2 == 1 or n < 6 or n > 1000000:
        break

    if gold_bach(n):
        print("Goldbach's conjecture is wrong.")