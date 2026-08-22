x = list(map(int, input().split()))
y= list(map(int, input().split()))
z=[]
for i in range(len(x)):
  z.append(x[i]+y[i])

print("vector_addition",z)
