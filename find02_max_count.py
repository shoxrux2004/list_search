def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    a=sorted(data)
    if a[-1]==a[-2]:
        return 2
    else:
        return 1
print(find_max_count([1,4,8,3,8,5]))
print(find_max_count([12,4,5,6,5]))