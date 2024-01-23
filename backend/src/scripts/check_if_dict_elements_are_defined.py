def check_if_dict_elements_are_defined(dictionnary):
    i = 0
    dictionnary_items = [*dictionnary.items()]
    while i < len(dictionnary_items)-1 and dictionnary_items[i][1] is not None:
        i+=1
    if (dictionnary_items[i][1] is None):
        return [False, dictionnary_items[i][0]]
    else:
        return [True, None]