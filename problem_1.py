def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None or number < 0:
        return None

    if number == 0 or number == 1:
        return number

    left = 1
    right = number
    while left <= right:
        x = left + (right - left) // 2
        if x * x == number:
            # we got luck and found it exact
            return x
        elif x * x < number:
            left = x + 1
        else:
            right = x - 1
    #if left * left > number:
    #    return left - 1
    return right

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# negative number test case
print("Pass" if (None == sqrt(-1)) else "Fail")

# none test case
print("Pass" if (None == sqrt(None)) else "Fail")

# large number test case
print("Pass" if (3162 == sqrt(10000000)) else "Fail")

# irrational number
print("Pass" if (1 == sqrt(2)) else "Fail")

