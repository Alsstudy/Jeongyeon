import sys
import itertools

li = list(int(sys.stdin.readline()) for i in range(9))
li.sort()


def get_list(li):
    re = sum(li) - 100
    for i in range(8, 0, -1):
        for j in range(i):
            if li[i] + li[j] == re:
                li.pop(i)
                li.pop(j)
                return li


sol = get_list(li)
for i in range(len(sol)):
    print(sol[i])


# # 더 간단한 코드 ..
# for i in itertools.combinations(li, 7):
#     if sum(i) == 100:
#         for j in sorted(i):
#             print(j)
#         break