def map_testing(foo, iterable):
    result = []
    for i in iterable:
        result.append(foo(i))
    return result