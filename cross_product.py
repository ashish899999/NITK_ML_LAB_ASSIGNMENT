x = list(map(int, input().split()))
y= list(map(int, input().split()))
def cross_product(a, b):
    c1 = a[1] * b[2] - a[2] * b[1]
    c2 = a[2] * b[0] - a[0] * b[2]
    c3 = a[0] * b[1] - a[1] * b[0]

    return [c1, c2, c3]


a = [1, 2, 3]
b = [4, 5, 6]

result = cross_product(a, b)

print(result)
