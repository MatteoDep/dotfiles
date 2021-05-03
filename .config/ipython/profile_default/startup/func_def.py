"""Useful function for ipython."""


def p(*args):
    """Print in scientific notation."""
    for arg in args:
        if isinstance(arg, str):
            print(arg)
        elif isinstance(arg, list):
            p(*arg)
        else:
            print("{:.3e}".format(arg))
