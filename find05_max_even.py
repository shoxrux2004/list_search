def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    l=[]
    for i in range(len(data)):
        if data[i]%2==0:
            l.append(data[i])
    return max(l)
print(find_max_even(data=[1,2,3,4,5]))
