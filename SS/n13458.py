n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = 0

for i in range(n):
    a[i] = max(a[i]-b, 0)
    cnt += 1

if sum(a) != 0:
    for i in range(n):
        if a[i] % c == 0:
            cnt += a[i] // c
        else:
            cnt += a[i] // c + 1

print(cnt)
