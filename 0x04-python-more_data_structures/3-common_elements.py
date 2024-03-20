def common_elements(set_1, set_2):
    """
    A function that returns a set of
    common elements in two sets
    """
    common = set()
    for element in set_1:
        if element in set_2:
            common.add(element)
    return common
