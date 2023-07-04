def counter():
    count = 0

    def in_counter():
        nonlocal count
        count+=1
        return count
    
    return in_counter

        