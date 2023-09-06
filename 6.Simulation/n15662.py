def move(n, d):
    global cur_left, cur_right, arr
    temp = d

    for i in reversed(range(n)):
        if arr[i][2] != cur_left:
            cur_left = arr[i][6]
            d *= -1
            rotate(arr[i], d)
        else:
            break

    d = temp
    for i in range(n+1, t):
        if arr[i][6] != cur_right:
            cur_right = arr[i][2]
            d *= -1
            rotate(arr[i], d)
        else:
            break


def rotate(li, d):
    if d == 1:
        q = li.pop()
        li.insert(0, q)
        return

    elif d == -1:
        q = li.pop(0)
        li.append(q)
        return


t = int(input())
arr = [list(map(int, input())) for _ in range(t)]
k = int(input())
for _ in range(k):
    n, d = map(int, input().split())
    cur_left, cur_right = arr[n-1][6], arr[n-1][2]
    rotate(arr[n-1], d)
    move(n-1, d)

print(sum([1 if val[0] else 0 for idx, val in enumerate(arr)]))