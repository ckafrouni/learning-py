def array_search(array, target):
    if len(array) == 0:
        raise ValueError
    index = len(array)//2
    while (len(array) and array[index] != target):
        if (array[index] < target):
            array = array[:index]
            index = len(array)//2
        else:
            array = array[index+1:]
            index = len(array)//2
    return index