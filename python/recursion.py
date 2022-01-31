def factorial(n):
    pass


def bunny_ears(n):
    if n == 1:
        return 2
    else:
        return bunny_ears(n-1) + 2

    '''
    Count recursively the number of bunny ears that would be if we had
    n bunnies.
    n >= 1
    bunny_ears(4) = 6 bunny ears
    '''
    pass


def powern(base,power):
    if power == 0:
        return 1
    else:
        return base * powern(base, power-1)
    """
    Given base and n that are both 0 or more, compute recursively (no loops) the value of
    base to the n power, so powerN(3, 4) is 81 (3^4).
    """
    pass


def array6(array, start=0):
    """
    Given an array of ints, compute recursively if the array contains a 6.
    We'll use the convention of considering only the part of the array that begins at the
    given index. In this way, a recursive call can pass index+1 to move down the array.
    The initial call will pass in index as 0.
    """
    pass


def countX(string, index=0):
    '''
    Given a string that we'll treat as an array of characters, compute recursively
    the number of times x that appear in the string.
    '''
    pass


def no_x(string, index=0):
    """
    Given a string, compute recursively a new string where all the 'x' chars have
    been removed.
    """
    pass


print("factorial 4 is",factorial(4))
print("bunny ears 3 is ", bunny_ears(3))
print("powern of 2 0 is",powern(2,0))
print("powern of 4 4 is",powern(4,4))
print("array6 [1,2,3,4,5,6]",array6([1,2,3,4,5,6]))
print("array6 [1,2,3,4,5]",array6([1,2,3,4,5]))
print("array6 [6]",array6([6]))
print("countX xxhixx is", countX("xxhixx"))
print("countX hi is", countX("hi"))
print("no_x xxhixx is", no_x("xxhixx"))
print("no_x hi is", no_x("hi"))
