def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    l=[]
    for i in range(len(data)):
        if data[i]%2==1:
            l.append(data[i])
    return min(l)
print(find_min_odd(data=[3,2,7,4,6]))