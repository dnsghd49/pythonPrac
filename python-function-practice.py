def max_num(a, b, c):
    return max([a, b, c])


print(max_num(100, 1, 2))


def mult_list(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


# Driver code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(mult_list(list1))
print(mult_list(list2))


def rev_string(my_string):
    return my_string[::-1]


print(rev_string("MACBOOK PRO"))


def num_within(a, b, c):
    return a in range(b, c+1)


print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))

# pascal(1)
# '''
# output:
# 1
# '''

# pascal(5)
# '''
# output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# '''
