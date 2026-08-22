x = list(map(int, input().split()))
y= list(map(int, input().split()))

dot_product=sum(x1*y1 for x1,y1 in zip(x,y))
print(dot_product)
