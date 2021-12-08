from library.permutations import Permutations, create_all_permutations
print("Посчитаем правую часть:")

A = Permutations([1, 4, 5, 2, 8, 7, 3, 6])
B = Permutations([4, 6, 8, 1, 2, 5, 3, 7])

C = (A.get_reverse() * (B ** 15)) ** 154
print(C)
print("Теперь решим уравение: ")
print("X * ")
Y = Permutations.create_from_cycles([[2, 7, 6], [3, 4], [5, 8], [1]])
print(Y)
print("* X = ")
print(C)
print(":")

answer = []
all = []
create_all_permutations(8, [], all)
for x in all:
    X = Permutations([i+1 for i in x])
    F = Permutations([])
    for i in range(1, 9):
        F[i] = X[Y[X[i]]]
    if F == C:
        answer.append(X)
for i in answer:
    print(i)
    print()
