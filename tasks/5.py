from library.matrix import Matrix

A = Matrix([[-1, 1], [3, -3], [-3, 3], [4, -4], [1, -1]])
B = Matrix([[3, 1, -1, -2, 2], [2, -3, 1, 3, -1]])
print("A * B =")
print(A * B)
print("Хар многочлен: ")
print((A * B).get_characteristic_polynomial())