n = int(input())
sum = 0

for i in range(1, n+1):
    sum += i * (n//i)

print(sum)