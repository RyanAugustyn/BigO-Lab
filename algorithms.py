#Task 1 
# Big O is constant time (always same number of steps)
def even_or_odd(num): 
    if num % 2 == 0:
        return True
    else:
        return False

#Task 2 
#Big O is linear time, as list grows have to check each value
def more_than_100(list):
    for num in list:
        if num >= 100:
            return False
    return True

#Task 3
#Big O is n^2 or quadratic time (two nested loops)
def are_repeats(list):
    for x in range(len(list)):
        for y in range(x + 1, len(list)):
            if list[x] == list[y]:
                return True
    return False

#Task 4 (done in previous lab)
#Big O of n^2 (two nested loops)
def sort_num_list(input_list): 
    new_list = []
    temp = 0
    while (len(input_list)) > 0: 
        temp = input_list[0]
        for x in range(len(input_list)):
            if temp > input_list[x]: 
                temp = input_list[x]
        new_list.append(temp)
        input_list.remove(temp)
    return new_list


# ex = sort_num_list([100, 20,7, -4, 80, 4])
# print(ex)




