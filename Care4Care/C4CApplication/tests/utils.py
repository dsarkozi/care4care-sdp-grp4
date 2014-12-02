from pprintpp import pprint as pp


def printy(*args):
    for arg in args:
        if hasattr(arg, '__dict__'):
            pp(arg.__dict__)
        else:
            pp(arg)

def printy_set(*args):
    for arg in args:
        for item in arg:
            pp(item.__dict__)