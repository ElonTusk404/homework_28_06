def zip_testing(*iterables):
    result = []
    minlen = min(len(item) for item in iterables)
    for i in range(minlen):
        items = tuple(item[i] for item in iterables)
        result.append(items)
    return result





