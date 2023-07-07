def enumerate_testing(arg, start=0):
    for i in range(len(arg)):
        yield (i + start, arg[i])