m,  n = map(int, input().split())

li = [True] * (n + 1)
li[0] = False
li[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if li[i]:
        for j in range(i * 2, n + 1, i):
            li[j] = False

for i in range(m, n + 1):
    if li[i]:
        print(i)