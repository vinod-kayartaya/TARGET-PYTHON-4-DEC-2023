def dirr(obj):
    """
    A convenient method to get a list of all non-dunder attributes of a given object

    :param obj: the object of which you want the attributes
    :return: a list consisting of attribute names
    """
    return [at for at in dir(obj) if not at.startswith('_')]


def factorial(num: int) -> int:
    if num <=0:
        raise ValueError('Only positive input was expected')

    f = 1
    for i in range(2, num+1):
        f *= i
    return f
