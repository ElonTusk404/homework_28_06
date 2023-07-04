def filter(foo, list):
    result = []
    for item in list:
        if foo(item):
            result.append(item)
    return result

