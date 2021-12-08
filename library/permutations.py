class Permutations:
    def __init__(self, permutation):
        self.permutation = {}
        for i in range(1, len(permutation) + 1):
            self.permutation[i] = permutation[i-1]

    @staticmethod
    def create_from_cycles(cycles):
        ans = Permutations([])
        ans.permutation = {}
        for cycle in cycles:
            for i in range(len(cycle)):
                ans.permutation[cycle[i]] = cycle[(i + 1) % len(cycle)]
        return ans

    @staticmethod
    def create_identity(n):
        return Permutations([i for i in range(1, n + 1)])

    def __iter__(self):
        return iter(self.permutation)

    def __repr__(self):
        first = []
        second = []
        for i in range(1, len(self.permutation) + 1):
            first.append(i)
            second.append(self.permutation[i])
        return str(first) + "\n" + str(second)

    def __getitem__(self, item):
        return self.permutation[item]

    def __setitem__(self, key, value):
        self.permutation[key] = value

    def __mul__(self, other):
        ans = Permutations([])
        for i in other:
            ans[i] = self[other[i]]
        return ans

    def get_reverse(self):
        ans = Permutations([])
        for i in self:
            ans[self[i]] = i
        return ans

    def __pow__(self, power, modulo=None):
        ans = self.create_identity(len(self.permutation))
        for i in range(power):
            ans = ans * self
        return ans

    def __eq__(self, other):
        return self.permutation == other.permutation


def create_all_permutations(n, now, answer):
    if len(now) == n:
        answer.append(now)
        return
    for i in range(n):
        if i not in now:
            create_all_permutations(n, now + [i], answer)


def get_sign(permutation):
    n = len(permutation)
    count_inversions = 0
    for i in range(n):
        for j in range(i):
            if permutation[j] > permutation[i]:
                count_inversions += 1
    if count_inversions % 2:
        return -1
    else:
        return 1