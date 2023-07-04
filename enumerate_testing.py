def enumerate_testing(arg, start=0):
    result = []
    for i in range(len(arg)):
        result.append((i + start, arg[i]))
    return result
