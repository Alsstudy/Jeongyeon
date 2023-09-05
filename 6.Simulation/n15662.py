# undo
def check_rotate(n, d):
    global arr
    od = d
    curl, curr = arr[n][2], arr[n][6]

    for i in reversed(range(n)):
        print(i)
        if curr != arr[i][2]:
            curr = arr[i][6]
            rotate(arr[i], d*-1)
            d *= -1
        else:
            break

    d = od
    for i in range(n+1, t):
        print(i)
        if curl != arr[n][6]:
            curl = arr[i][2]
            rotate(arr[i], d*-1)
            d *= -1
        else:
            break
    print()
    print()

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
    check_rotate(n-1, d)

print(arr)