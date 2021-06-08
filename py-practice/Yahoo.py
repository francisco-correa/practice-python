my_list = [ 1, 0, 0, 0, 1, 0, 0, 0, 1, 1 ]

def my_function(numbers):
    new_list = []
    for numb in numbers:
        if my_list[numb] == 0:
            return new_list.append("Yahoo")
        else:
            return new_list.append("1")
    return new_list

print(my_function(my_list))

