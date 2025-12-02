m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[7, 8], [9, 10], [11, 12]]
result = [[sum(m1[i][k] * m2[k][j] for k in range(len(m2))) for j in range(len(m2[0]))] for i in range(len(m1))]
print("Matrix1:", m1)
print("Matrix2:", m2)
print("Multiplication result:", result)
