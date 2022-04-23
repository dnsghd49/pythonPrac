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

triangle = [[1], [1, 1]]


def pascal(n):
    # base case
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        # fill up correct number of rows in triangle
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            # create correct row, then add to triangle (this row will be 1 longer than row before it)
            length = len(row_prev)+1
            for i in range(length):
                # first number is 1
                if i == 0:
                    row.append(1)
                # intermediate nunmbers get added from previous rows
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1]
                               [i-1]+triangle[row_number-1][i])
                # last number is 1
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        # print triangle
        for row in triangle:
            print(row)


pascal(0)
pascal(1)
# '''
# output:
# 1
# '''

pascal(5)
# '''
# output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# '''
