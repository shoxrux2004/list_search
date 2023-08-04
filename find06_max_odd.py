def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    l=[]
    for i in range(len(data)):
        if data[i]%2==1:
            l.append(data[i])
    return max(l)
print(find_max_odd(data=[1,2,7,4,6]))