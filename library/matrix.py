from library.permutations import create_all_permutations, get_sign


def get_combinations(n, m, answer, now=(), index=0):
    if len(now) == m:
        answer.append(now)
        return
    if index >= n:
        return
    get_combinations(n, m, answer, now + (index,), index+1)
    get_combinations(n, m, answer, now, index+1)


class Polynomial:
    def __init__(self, rations):
        self.rations = rations

    def __repr__(self):
        answer = ""
        for deg in range(len(self.rations) - 1, -1, -1):
            answer += str(self.rations[deg]) + "*x^" + str(deg) + " + "
        return answer


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
        return Polynomial(answer)

    @staticmethod
    def get_id(n):
        rows = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        return Matrix(rows)
