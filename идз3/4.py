from library.matrix import Matrix

A = Matrix([[-1, 0, -3,  2], [4, -1, 6, -2], [4, -1, 7, -3], [4, -1, 7, -3]])
print(A.get_characteristic_polynomial())
print((A - Matrix.get_id(4)) * (A - Matrix.get_id(4)))
print(A)
print(A * A)
