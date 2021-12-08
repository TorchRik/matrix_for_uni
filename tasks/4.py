from library.matrix import Matrix
from library.permutations import create_all_permutations, get_sign

x = 1  # Просто создадим матрицу с целыми коэффицентами
A = Matrix([[6, x, 9, -1, 1, -5, -6],
            [9, -6, -4, -5, 4, x, -3],
            [-8, 7, -9, x, -8, -7, -9],
            [-8, -5, -2, 1, -5, -2, x],
            [-4, 9, 5, 2, -8, 2, x],
            [1, -9, x, -6, x, -3, 1],
            [x, 9, -1, 9, 3, -4, -5]])
x_coordinates = [[1], [5], [3], [6], [6], [2, 4], [0]]  # кординаты x в матрице

permutations = []
create_all_permutations(7, [], permutations)
answer = 0
for permutation in permutations:
    count = 0
    s = 1
    for i in range(7):
        if permutation[i] in x_coordinates[i]:
            count += 1
        s *= A[i][permutation[i]]
    if count == 5:
        print(permutation, s)
        answer += s * get_sign(permutation)
print("Ответ:", answer)

