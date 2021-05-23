def get_min_max(ints):

    if ints is None or len(ints) == 0:
        return (None, None)

    # begin with min and max set to first element
    mn = ints[0]
    mx = ints[0]

    # begin at index 1
    for i in range(1, len(ints)):
        n = ints[i]
        if n < mn:
            mn = n
        if n > mx:
            mx = n

    return (mn, mx)


def test_function(ints):
    min_and_max = get_min_max(ints)

    if ints is None or len(ints) == 0:
        s = (None, None)
    elif len(ints) == 1:
        s = (ints[0], ints[0])
    else:
        s = sorted(ints)
        s = (s[0], s[len(s) - 1])
    # print('m = {}, s = {}'.format(min_and_max, s))
    if min_and_max == s:
        print("Pass")
    else:
        print("Fail")

# sorted ascending case
test_function([1, 2, 3, 4, 5, 6])

# test random input
import random
l = [i for i in range(0, 10)]
random.shuffle(l)
test_function(l)

# test empty list
test_function([])

# test None list
test_function(None)

# test single element
test_function([100])

# test when min and max are same
test_function([100, 100])

# test negative input
test_function([-100, -100])

# test negative and positive
test_function([-100, 1, 1, 1, 1, 1, 1, 1, 1, 100])



