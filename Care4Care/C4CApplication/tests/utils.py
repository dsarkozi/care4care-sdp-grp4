from pprintpp import pprint as pp


def printy(*args):
    for arg in args:
        pp(arg.__dict__)

def printy_set(*args):
    for arg in args:
        for item in arg:
            pp(item.__dict__)