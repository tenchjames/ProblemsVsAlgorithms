
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if None == input_list or len(input_list) == 0 or None == number:
        return -1

    left = 0
    right = len(input_list) - 1;

    # find the index of the lowest element
    # this is O(log n)
    while left < right:
        mid = left + (right - left) // 2
        if input_list[mid] == number:
            # we got lucky and found it
            return mid
        elif input_list[mid] > input_list[right]:
            # the array is shifted and lowest point is more right
            left = mid + 1
        else:
            right = mid
    # decide what side to begin searching in normal binary search form
    # left and right pointers crossed 
    # print('left = {}, right = {}'.format(left, right))
    if input_list[len(input_list) - 1] >= number:
        right = len(input_list) - 1
    else:
        left = 0;

    # normal binary search
    # O(log n)
    while left <= right:
        mid = left + (right - left) // 2;
        if input_list[mid] == number:
            return mid
        elif input_list[mid] > number:
            right = mid -1
        else:
            left = mid + 1

    # not found if we got here
    return - 1

def linear_search(input_list, number):
    if None == input_list or None == number:
        return -1

    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    l = linear_search(input_list, number)
    rs = rotated_array_search(input_list, number)
    # print('ls = {}, rs = {}'.format(l, rs))
    if l == rs:
        print("Pass")
    else:
        print("Fail")

# find element at start
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])

# find element that is smallest of list
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])

# find element that is largest of list
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 10])

# find in even number of elements
test_function([[6, 7, 8, 1, 2, 3], 8])

# find lowest in even number of elements
test_function([[6, 7, 8, 1, 2, 3], 1])

# find in empty list
test_function([[], 10])

# find in None list
test_function([None, 100])

# find None
test_function([[1, 2, 3, 0], None])

