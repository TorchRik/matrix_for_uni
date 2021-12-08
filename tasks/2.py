from library.matrix import Matrix

A = Matrix([[-2, 3, -2, -1], [-3, 1, 1, -1], [2, -1, -3, 1], [-3, -2, 3, 1]])
B = Matrix([[6, -6, 10, 6], [-10, -2, 9, -1], [4, -8, 9, 1], [2, 7, 9, -9]])
C = Matrix([[-1, -3, 3, 1], [-1, 3, 3, -1], [2, -1, -2, -3], [-2, 2, 2, 1]])
D = Matrix([[-1, 1, -1, -1], [-1, 2, -2, -2], [1, -2, 3, 3], [-1, 2, -1, -2]])

print("A * (X + B) ^ (-1) * C = D")
print("det(A) = " + str(A.get_determinant()))
print("det(C) = " + str(C.get_determinant()))
print("det(D) = " + str(D.get_determinant()))
print("Детерминанты не 0, значит можем спокойно брать обратные и преоброзовать к виду")
print("X = C * D^(-1) * A - B")
print("X = ")
X = C * D.get_reverse() * A - B
print(X)
