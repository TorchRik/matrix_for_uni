from library.matrix import Matrix
A = Matrix([[-2, 4, -3, -4], [-1, 3, 2, 2], [-1, 3, 1, 2], [0, 0, -2, -3]])

print("Хар многочлен: " + str(A.get_characteristic_polynomial()))

print("(A^2 + 3 * A + 2)^(-2) = ")
x = (A * A + A * 3 + 2).get_reverse()
print(x.get_determinant() ** 2)

