from library.matrix import Matrix

C = Matrix([[1, 3, 2], [2, 5, 5], [1, -5, 5]])

C_rev = C.get_reverse()
print(C_rev)
print(C * C_rev)

C2 = Matrix([[2, 1, -1], [-3, 2, -3], [2, 0, 0]])
print(C2.get_reverse())
print(C2 * C2.get_reverse())

A_2 = Matrix([[3, -3, 1], [-1, 5, -2], [1, 2, 4]])
print(C2 * A_2 * C2.get_reverse())
A_1 = Matrix([[-4, 3, 3], [1, 5, 2], [4, 4, -4]])

print(C * A_1 * C.get_reverse())
print(C2.get_reverse() * C)

F = Matrix([[-35,  -3, -4],
        [-8, 13, -19],
        [-6, -6 , 2]])
A = F * C2.get_reverse()
print(A)

