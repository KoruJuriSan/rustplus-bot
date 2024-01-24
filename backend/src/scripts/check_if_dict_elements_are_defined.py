def check_if_dict_elements_are_defined(dictionnary):
    """Check for every value in the dictionnary, and tell if one of the value is == to None

    Args:
        dictionnary (dict): the dictionnary to check
    
    Returns:
        [bool, dictionnary_value || None]
        bool: if there is any Undefined (None) value in a dictionnary"
        dictionnary_value: if there is an Undefined (None) value, the key of this item in the dictionnary
    """
    i = 0
    dictionnary_items = [*dictionnary.items()]
    while i < len(dictionnary_items)-1 and dictionnary_items[i][1] is not None:
        i+=1
    if (dictionnary_items[i][1] is None):
        return [False, dictionnary_items[i][0]]
    else:
        return [True, None]