from math import gcd

from library.permutations import create_all_permutations, get_sign
from library.polynomial import Polynomial


def sign_integer(a):
    if a < 0:
        return -1
    else:
        return 1


def get_combinations(n, m, answer, now=(), index=0):
    if len(now) == m:
        answer.append(now)
        return
    if index >= n:
        return
    get_combinations(n, m, answer, now + (index,), index+1)
    get_combinations(n, m, answer, now, index+1)


class Matrix:
    def __init__(self, rows):
        self.n = len(rows)
        if self.n == 0:
            self.m = 0
            self.rows = []
            return
        self.m = len(rows[0])
        for row in rows:
            if len(row) != self.m:
                raise AttributeError("Rows should have same size")
        self.rows = [row[:] for row in rows]

    def __getitem__(self, index):
        return self.rows[index]

    def __setitem__(self, key, value):
        self.rows[key] = value

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.n != other.n or self.m != other.m:
                raise AttributeError("Cannot fold matrix")
            rows = [[0 for i in range(self.m)] for i in range(self.n)]
            for i in range(self.n):
                for j in range(self.m):
                    rows[i][j] = self[i][j] + other[i][j]
            return Matrix(rows)

        elif isinstance(other, int) or isinstance(other, float):
            rows = [[0 for i in range(self.m)] for i in range(self.n)]
            for i in range(self.n):
                for j in range(self.m):
                    rows[i][j] = other + self[i][j]
            return Matrix(rows)

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.n != other.n or self.m != other.m:
                raise AttributeError("Cannot sub matrix")
            rows = [[0 for i in range(self.m)] for i in range(self.n)]
            for i in range(self.n):
                for j in range(self.m):
                    rows[i][j] = self[i][j] - other[i][j]
            return Matrix(rows)
        elif isinstance(other, Matrix):
            rows = [[0 for i in range(self.m)] for i in range(self.n)]
            for i in range(self.n):
                for j in range(self.m):
                    rows[i][j] = self[i][j] - other
            return Matrix(rows)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.m != other.n:
                raise AttributeError("Cannot multiple matrix")
            rows = [[0 for i in range(other.m)] for i in range(self.n)]
            for i in range(self.n):
                for j in range(other.m):
                    for k in range(self.m):
                        rows[i][j] += self[i][k] * other[k][j]
            return Matrix(rows)
        elif isinstance(other, int) or isinstance(other, float):
            rows = [[0 for i in range(self.m)] for i in range(self.n)]
            for i in range(self.n):
                for j in range(self.m):
                    rows[i][j] = other * self[i][j]
            return Matrix(rows)

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            rows = [[0 for i in range(self.m)] for i in range(self.n)]
            for i in range(self.n):
                for j in range(self.m):
                    rows[i][j] = self[i][j] / other
            return Matrix(rows)

    def __eq__(self, other):
        return self.rows == other.rows

    def __pow__(self, power, modulo=None):
        if self.n != self.m:
            raise ValueError("Matrix should be square")

        answer = Matrix.get_id(self.n)
        for i in range(power):
            answer *= self
        return answer

    def get_string_for_latex(self):
        out = ""
        for row in self.rows:
            for i in row:
                out += str(i) + " & "
            out = out[:-2]
            out += "\\\\\n"

        return "\\begin{align*} \\begin{pmatrix}" + out  + "\end{pmatrix} \end{align*}"

    def __repr__(self):
        out = ""
        for row in self.rows:
            for i in row:
                out += str(i) + " "
            out += "\n"
        return out

    def get_determinant(self):
        if self.n != self.m:
            raise AttributeError("It is not square matrix")
        permutations = []
        create_all_permutations(self.n, [], permutations)
        determinant = 0
        for permutation in permutations:
            now = get_sign(permutation)
            for i in range(self.n):
                now *= self[i][permutation[i]]
            determinant += now
        return determinant

    def get_algebraic_complement(self, i, j):
        new_rows = [[0 for i in range(self.m - 1)] for i in range(self.n - 1)]
        for i1 in range(self.n):
            for j1 in range(self.m):
                if i1 == i or j1 == j:
                    continue
                i2 = i1 if i1 < i else i1 - 1
                j2 = j1 if j1 < j else j1 - 1
                new_rows[i2][j2] = self[i1][j1]
        mult = -1 if (i + j) % 2 else 1
        return mult * Matrix(new_rows).get_determinant()

    def get_attached_matrix(self):
        rows = [[0 for i in range(self.m)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                rows[i][j] = self.get_algebraic_complement(j, i)
        return Matrix(rows)

    def get_reverse(self):
        attached_matrix = self.get_attached_matrix()
        return attached_matrix / self.get_determinant()

    def get_characteristic_polynomial(self):
        answer = []
        for k in range(self.n):
            combinations = []
            get_combinations(self.n, k, combinations)
            a_k = 0
            for combination in combinations:
                rows = []
                for i in range(self.n):
                    if i in combination:
                        continue
                    rows.append([])
                    for j in range(self.m):
                        if j in combination:
                            continue
                        rows[-1].append(self[i][j])
                a_k += Matrix(rows).get_determinant()
            a_k *= (-1) ** (self.n - k)
            answer.append(a_k)
        answer.append(1)
        answer.reverse()
        return Polynomial(answer)

    def __copy__(self):
        return Matrix([row[:] for row in self.rows])

    @staticmethod
    def get_id(n):
        rows = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        return Matrix(rows)

    def multiply_row_by_num(self, row_index, x):
        if row_index >= self.n:
            raise ValueError("Invalid index")

        for j in range(self.m):
            self.rows[row_index][j] *= x

    def do_gaus_with_integer_matrix_and_get_rank(self):
        for i in range(self.n):
            for j in range(self.m):
                if not isinstance(self[i][j], int):
                    raise ValueError("Matrix should contain only integers")

        A = self.__copy__()
        current_row_index = 0
        for j in range(A.m):
            if current_row_index >= A.n:
                break
            for i in range(current_row_index, A.n):
                if A[i][j] != 0:
                    A[i], A[current_row_index] = A[current_row_index], A[i]
                    break

            if A[current_row_index][j] != 0:
                for i in range(A.n):
                    if i == current_row_index or A[i][j] == 0:
                        continue
                    g = gcd(A[current_row_index][j], A[i][j])
                    mult_1 = abs(A[current_row_index][j])
                    mult_2 = abs(A[i][j]) // g
                    A.multiply_row_by_num(i, mult_1 // g)
                    s = sign_integer(A[current_row_index][j]) * sign_integer(A[i][j])
                    for u in range(A.m):
                        A[i][u] -= A[current_row_index][u] * s * mult_2
                current_row_index += 1  # increase such as we found non-zero row
        return A, current_row_index

    def get_rank(self):
        return self.do_gaus_with_integer_matrix_and_get_rank()[1]
