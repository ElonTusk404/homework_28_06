def filter(foo, list):
    for item in list:
        if foo(item):
            yield (item)

