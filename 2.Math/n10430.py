A, B, C = map(float, input().split())

print(int((A + B) % C))
print(int(((A % C) + (B % C)) % C))
print(int((A * B) % C))
print(int(((A % C) * (B % C)) % C))
