def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    l=[]
    for i in range(len(data)):
        if data[i]%2==0:
            l.append(data[i])
    return min(l)
print(find_min_even(data=[1,2,7,4,6]))