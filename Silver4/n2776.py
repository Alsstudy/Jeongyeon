import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    s1 = int(input())
    num1 = set(map(int, input().split()))
    s2 = int(input())
    num2 = list(map(int, input().split()))
    for num in num2:
        if num in num1:
            print(1)
        else:
            print(0)