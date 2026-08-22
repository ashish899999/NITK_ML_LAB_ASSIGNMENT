row_a=int(input("Rows OF A:"))
col_a=int(input("cols of A:"))

row_=bint(input("Rows OF B:"))
col_b=int(input("cols of B:"))

A=[list(map(int,input().split() for _ in range(row_a))
B=[list(map(int,input().split() for _ in range(row_b))

rows=len(A)
cols=len(A[0])
C=[[0]*cols for _ in range(rows)]
for i in range(rows):
  for j in range(cols):
    C[i][j]=A[i][j]+ B[i][j]

print(C)
