N = int(input())
li = list(map(int, input().split()))

sum = 0

for i in li:
    m = 1
    if i != 1:
        for j in range(2, i):
            if i != 1 and i % j == 0:
                m = 0
        if m == 1:
            sum += 1

print(sum)