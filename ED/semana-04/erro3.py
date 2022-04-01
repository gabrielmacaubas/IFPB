def d():
    raise IndexError()


def c():
    v = d()
    if v == -1:
        return -1


def b():
    v = c()
    if v == -1:
        return -1


def a():
    try:
        v = b()
    except IndexError:
        print("deu erro")


a()
