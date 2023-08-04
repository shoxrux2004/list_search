def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    a=sorted(data)
    if a[0]==a[1]:
        return 2
    else:
        return 1
print(find_min_count([2,5,9,11,6,3]))
print(find_min_count([0,-4,3,9,-2,-4]))