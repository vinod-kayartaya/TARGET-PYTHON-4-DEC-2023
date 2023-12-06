def dirr(obj):
    """
    A convenient method to get a list of all non-dunder attributes of a given object

    :param obj: the object of which you want the attributes
    :return: a list consisting of attribute names
    """
    return [at for at in dir(obj) if not at.startswith('_')]

