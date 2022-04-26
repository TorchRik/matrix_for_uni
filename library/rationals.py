from math import gcd


def sign(x):
    return 1 if x > 0 else -1


class Rational:
    def __init__(self, whole, divider=1):
        if isinstance(whole, Rational):
            self._whole = whole._whole
            self._divider = whole._divider
        else:
            if not isinstance(whole, int) or not isinstance(divider, int):
                raise ValueError("Divider and whole part should be integer")
            if divider <= 0:
                raise ValueError("Divider should be greater then 0")
            self._whole = whole
            self._divider = divider

    def __add__(self, other):
        result = Rational(self._whole, self._divider)
        if isinstance(other, int):
            result._whole += other * result._divider
            return result
        elif isinstance(other, Rational):
            result._whole *= other._divider
            result._whole += other._whole * result._divider
            result._divider *= other._divider
            return result
        else:
            raise ValueError("Incorrect addition, possible addition only with int, and Rational")

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        result = Rational(self._whole, self._divider)
        if isinstance(other, int):
            result._whole *= other
            return result
        elif isinstance(other, Rational):
            result._whole *= other._whole
            result._divider *= other._divider
            return result
        else:
            raise ValueError("Incorrect multiplication, possible multiplication only with int, and Rational")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        return self + (-1 * other)

    def __rsub__(self, other):
        return other + (-1 * self)

    def __truediv__(self, other):
        result = Rational(self._whole, self._divider)
        if isinstance(other, int):
            if other == 0:
                raise ValueError("Division by 0")
            result._divider *= abs(other)
            result._whole *= sign(other)
            return result
        elif isinstance(other, Rational):
            result._whole *= other._divider
            result /= other._whole
            return result
        else:
            raise ValueError("Incorrect division, possible division only with int, and Rational")

    def __rtruediv__(self, other):
        if isinstance(other, int):
            whole = other * self._divider * sign(self)
            divider = abs(self._whole)
            return Rational(whole, divider)
        return self.__truediv__(other)

    def __prepare_to_comparing(self, other):
        if isinstance(other, Rational):
            return self._whole * other._divider, other._whole * self._divider
        elif isinstance(other, int):
            return self._whole, other * self._divider
        else:
            raise ValueError("Incorrect comparing, possible compare only with int, and Rational")

    def __eq__(self, other):
        left, right = self.__prepare_to_comparing(other)
        return left == right

    def __le__(self, other):
        left, right = self.__prepare_to_comparing(other)
        return left <= right

    def __lt__(self, other):
        left, right = self.__prepare_to_comparing(other)
        return left < right

    def __ge__(self, other):
        left, right = self.__prepare_to_comparing(other)
        return left >= right

    def __gt__(self, other):
        left, right = self.__prepare_to_comparing(other)
        return left > right

    def __repr__(self):
        whole = self._whole // gcd(self._whole, self._divider)
        divider = self._divider // gcd(self._whole, self._divider)
        if divider == 1 or whole == 0:
            return f"{whole}"
        else:
            return f"{whole}/{divider}"

    def get_string_for_latex(self):
        whole = self._whole // gcd(self._whole, self._divider)
        divider = self._divider // gcd(self._whole, self._divider)
        if divider == 1 or whole == 0:
            return f"{whole}"
        else:
            return "\\fractial{" + str(self._whole) + "}{" + str(self._divider) + "}"
