
# problem set said to calculate in O(n log n) time 
# Can be done in O(n) as well
def rearrange_digits_ntime(input_list):

    if None == input_list or len(input_list) == 0:
        return [None, None]
    
    if len(input_list) == 1:
        return [input_list[0], 0]

    counts = [0 for x in range(0, 10)]

    for i in range(len(input_list)):
        counts[input_list[i]] += 1;

    n1 = ""
    n2 = ""
    is_even = True
    for i in range(9, -1, -1):
        current_count = counts[i]
        while current_count > 0:
            if is_even:
                n1 += str(i)
            else:
                n2 += str(i)
            is_even = not is_even
            current_count -= 1
    
    return (int(n1), int(n2))



# below for O(n log n) solution using quick sort

def swap(input_list, x, y):
    temp = input_list[x]
    input_list[x] = input_list[y]
    input_list[y] = temp


# help quick sort when arrays are already sorted

def median_of_3(input_list, left, right):
    mid = left + (right - left) // 2
    # move the elements so they are positioned
    # largest, mid, smallest
    
    if input_list[left] < input_list[mid]:
        swap(input_list, left, mid)

    if input_list[left] < input_list[right]:
        swap(input_list, left, right)

    if input_list[mid] < input_list[right]:
        swap(input_list, mid, right)

    # put our pivot one to the left of right
    # because right is already sorted
    swap(input_list, mid, right - 1)
    return input_list[right - 1]

def small_sort(input_list, left, right):
    n = right - left + 1

    if n <= 1:
        # already sorted
        return
    elif n == 2:
        if input_list[left] < input_list[right]:
            swap(input_list, left, right)
    else:
        mid = right - 1
        if input_list[left] < input_list[mid]:
            swap(input_list, left, mid)

        if input_list[left] < input_list[right]:
            swap(input_list, left, right)
        
        if input_list[mid] < input_list[right]:
            swap(input_list, mid, right)
        
def pivot(input_list, low, high, pivot_value):
    left = low
    right = high - 1

    while True:
        left += 1
        while input_list[left] > pivot_value:
            # move pointer
            left += 1
        
        right -= 1
        while right > 0 and input_list[right] < pivot_value:
            # move right pointer
            right -= 1
        
        if left >= right:
            break
        else:
            swap(input_list, left, right)

    swap(input_list, left, high - 1)
    return left


def r_quick_sort(input_list, low, high):
    size = high - low + 1;
    if size <= 3:
        small_sort(input_list, low, high)
    else:
        pivot_value = median_of_3(input_list, low, high)
        pivot_index = pivot(input_list, low, high, pivot_value)
        r_quick_sort(input_list, low, pivot_index -1)
        r_quick_sort(input_list, pivot_index + 1, high)

def quick_sort(input_list):
    r_quick_sort(input_list, 0, len(input_list) - 1)

def rearrange_digits(input_list):

    if None == input_list or len(input_list) == 0:
        return [None, None]

    if len(input_list) == 1:
        return [input_list[0], 0]

    # sorting will take O (n log n) time
    quick_sort(input_list)
    
    n1 = ""
    n2 = ""
    is_even = True

    for number in input_list:
        if is_even:
            n1 += str(number)
        else:
            n2 += str(number)
        is_even = not is_even
    
    return (int(n1), int(n2))

def test_function(test_case):
    n_output = rearrange_digits_ntime(test_case[0])
    output = rearrange_digits(test_case[0])
    solution = test_case[1]

    if None == test_case[0] or len(test_case[0]) == 0:
        if (solution[0] == n_output[0] and solution[1] == n_output[1] 
            and solution[0] == output[0] and solution[1] == output[1]):
            print("Pass")
        else:
            print("Fail")
    elif sum(n_output) == sum(solution) and sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# odd number of elements
test_function([[1, 2, 3, 4, 5], [542, 31]])

# even number of elements
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# empty list
test_function([[], [None, None]])


# none list
test_function([None, [None, None]])


# same element
test_function([[9, 9, 9, 9], [99, 99]])


# single element
test_function([[9], [9, 0]])


# two elements
test_function([[9, 8], [9, 8]])
