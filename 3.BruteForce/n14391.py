def bitmask():
    global maxVal
    for i in range(1 << n*m):
        total = 0
        for row in range(n):
            rowsum = 0
            for col in range(m):
                idx = row * m + col
                if i & (1 << idx) != 0:
                    rowsum = rowsum * 10 + li[row][col]
                else:
                    total += rowsum
                    rowsum = 0
            total += rowsum

        for col in range(m):
            colsum = 0
            for row in range(n):
                idx = row * m + col
                if i & (1 << idx) == 0:
                    colsum = colsum * 10 + li[row][col]
                else:
                    total += colsum
                    colsum = 0
            total += colsum

        maxVal = max(maxVal, total)


n, m = map(int, input().split())
li = [list(map(int, input())) for _ in range(n)]
maxVal = 0
bitmask()
print(maxVal)