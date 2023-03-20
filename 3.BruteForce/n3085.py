n = int(input())
li = [0] * n

for i in range(n):
    li[i] = list(input())


# 열 단위 count
def count_rows():
    global cnt_max
    for i in range(n):
        cnt_row = 1
        for j in range(n-1):
            if li[i][j] == li[i][j+1]:
                cnt_row += 1
                cnt_max = max(cnt_max, cnt_row)
            else:
                cnt_row = 1


# 행 단위 count
def count_cols():
    global cnt_max
    for i in range(n):
        cnt_col = 1
        for j in range(n-1):
            if li[j][i] == li[j+1][i]:
                cnt_col += 1
                cnt_max = max(cnt_max, cnt_col)
            else:
                cnt_col = 1


cnt_max = 0
for i in range(n):
    for j in range(n - 1):
        # 열 단위의 연속한 두 사탕 색깔이 다르다면 바꿔주기
        if li[i][j] != li[i][j + 1]:
            li[i][j], li[i][j + 1] = li[i][j + 1], li[i][j]  # 바꾸고
            count_rows()
            count_cols()
            li[i][j + 1], li[i][j] = li[i][j], li[i][j + 1]  # 되돌려놓기
        # 행 단위의 연속한 두 사탕 색깔이 다르다면 바꿔주기
        if li[j][i] != li[j + 1][i]:
            li[j][i], li[j + 1][i] = li[j + 1][i], li[j][i]  # 바꾸고
            count_rows()
            count_cols()
            li[j + 1][i], li[j][i] = li[j][i], li[j + 1][i]  # 되돌려놓기


print(cnt_max)