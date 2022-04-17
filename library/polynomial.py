from library.convector_to_latex_format import convert_polynomial_to_latex_view


class Polynomial:
    def __init__(self, rations):
        self.rations = rations
        self.degree = len(rations) - 1

    def __repr__(self):
        answer = ""
        for i in range(self.degree + 1):
            if answer != "" and self.rations[i] >= 0:
                answer += " + "
            answer += str(self.rations[i])
            deg = self.degree - i
            if deg != 0:
                answer += "*x ** " + str(deg)
        return answer

    def __copy__(self):
        return Polynomial(self.rations[:])

    def __getitem__(self, index):
        return self.rations[index]

    def __setitem__(self, key, value):
        self.rations[key] = value

    @classmethod
    def create_empty_polynomial(cls, degree):
        return cls([0 for i in range(degree + 1)])

    def __len__(self):
        return len(self.rations)

    def __floordiv__(self, other):
        if isinstance(other, Polynomial):
            if self.degree < other.degree:
                return self.create_empty_polynomial(0)
            answer = self.create_empty_polynomial(self.degree - other.degree)
            temporary_copy = self.__copy__()
            for i in range(len(answer)):
                k = temporary_copy[i] / other[0]
                answer[i] = k
                for j in range(len(other)):
                    temporary_copy[i+j] -= k * other[j]
            return answer
        elif isinstance(other, int) or isinstance(other, float):
            for i in range(len(self)):
                self[i] /= other
        else:
            raise TypeError("Incorrect type of divider")

    @convert_polynomial_to_latex_view
    def get_latex_view(self):
        return str(self)

    def substitute_x(self, x):
        return eval(str(self))

    def get_integer_roots_in_range(self, left, right):
        roots = []
        for i in range(left, right + 1):
            if self.substitute_x(i) == 0:
                roots.append(i)
        return roots