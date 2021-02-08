def average(array):
    if len(array) == 0:
        return 0
    
    total = 0
    for item in array:
        total += item
    return total / len(array)
