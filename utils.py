def str_eq(str1, list1):
    """Checks if str1 is contained in list1. Not case senstive"""
    list2 = []
    for item in list1:
        list2.append(item.lower())
    return str1.lower() in list2


def other(str1, list1):
    """Returns the list of all values in list1 except for str1"""
    list2 = []
    for item in list1:
        list2.append(item.lower())

    loc = list2.index(str1)
    del list1[loc]

    return list1


def other_str(str1, list1):
    """Returns the string of all vlaues in lis1 except for str1"""
    others = other(str1, list1)
    if len(others) == 0:
        return ''

    to_return = ''
    for item in others:
        to_return += f"{item}, "
    return to_return[0:-2]


def inc_str(list1):
    """Returns the string for an incorrect guess"""
    to_return = ''
    if len(list1) != 1:
        to_return += "one of "

    for item in list1:
        to_return += f"{item}, "

    return to_return[0:-2]
