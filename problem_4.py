
def sort_012(input_list):
    if input_list is None:
        return None

    counts = [0 for x in range(3)]

    for n in input_list:
        counts[n] += 1

    index = 0
    for i in range(len(counts)):
        count = counts[i]
        while count > 0:
            input_list[index] = i
            count -= 1
            index += 1

    return input_list


def test_function(test_case):
    output = sort_012(test_case)
    if None is test_case:
        expected = None
    else:
        expected = sorted(test_case)
    
    if output == expected:
        print("Pass")
    else:
        print("Fail")

# basic test cases
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# empty list test case
test_function([])

# None list test case
test_function(None)

# single element test case
test_function([2])

# big list
import random
l = []
for i in range(1000000):
    l.append(random.randint(0, 2))

test_function(l)






