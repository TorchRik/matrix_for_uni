def convert_polynomial_to_latex_view(fn):
    def get_latex_view(*args):
        python_view = fn(args[0])
        latex_view = "$" + python_view.replace("**", "^") + "$"
        return latex_view
    return get_latex_view
