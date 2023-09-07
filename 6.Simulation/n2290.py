import sys
input = sys.stdin.readline


def line(li, idx):
    for i in idx:
        if i == 1:
            for j in range(s):
                li[j+1][0] = '|'
        elif i == 2:
            for j in range(s):
                li[0][j+1] = '-'
        elif i == 3:
            for j in range(s):
                li[j+1][s+1] = '|'
        elif i == 4:
            for j in range(s+1, 2*s+1):
                li[j+1][0] = '|'
        elif i == 5:
            for j in range(s):
                li[2*s+2][j+1] = '-'
        elif i == 6:
            for j in range(s+1, 2*s+1):
                li[j+1][s+1] = '|'
        elif i == 7:
            for j in range(s):
                li[s+1][j+1] = '-'


s, n = map(int, input().split())
n = str(n)

info = {'0': [1, 2, 3, 4, 5, 6], '1': [3, 6], '2': [2, 3, 4, 5, 7], '3': [2, 3, 5, 6, 7], '4': [1, 3, 6, 7],
        '5': [1, 2, 5, 6, 7], '6': [1, 2, 4, 5, 6, 7], '7': [2, 3, 6], '8': [1, 2, 3, 4, 5, 6, 7], '9': [1, 2, 3, 5, 6, 7]}
answer = [[[' ' for i in range(s+2)] for j in range(2*s+3)] for k in range(len(n))]

for idx, num in enumerate(n):
    line(answer[idx], info[num])

for i in range(2*s+3):
    for j in range(len(n)):
        if j == len(n) - 1:
            print(''.join(answer[j][i]))
        else:
            print(''.join(answer[j][i]), end=' ')
