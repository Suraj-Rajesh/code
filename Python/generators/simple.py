def simple_generator():
    yield 1
    yield 2
    yield 3

for no in simple_generator():
    print no
    if 2 == no:
        break

for no in simple_generator():
    """ New one """
    print 'New one'
    print no
