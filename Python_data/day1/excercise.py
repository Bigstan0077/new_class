from Checks.checker import checks

@checks(str)
def string_checker(value,*args):
    ans = value
    return ans

@checks(int)
def integer_checker(value ,*args):
    ans = value
    return ans


@checks(bool)
def boolean_checker(value ,*args):
    ans = value
    return ans


@checks(list)
def List_checker(value ,*args):
    ans = value
    return ans


@checks(dict)
def dictionary_checker(value = None,*args):
    ans = value
    return ans


@checks(tuple)
def tuple_checker(value = None,*args):
    ans = value
    return ans


@checks(set)
def set_checker(value = None,*args):
    ans = value
    return ans

# -----------------------------------------------xxxxx Your answers xxxxx---------------->






if __name__ == '__main__':
    string_checker()             #`string`
    boolean_checker()             #`boolean
    integer_checker()           #`integer
    List_checker()               #list
    dictionary_checker()          # Dictionary
    tuple_checker()               #tuple
    set_checker()                 #set
