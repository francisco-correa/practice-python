list_of_numbers = [4,  80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]

#Your code here:
list_even = []
list_odd  = []
def merge_two_list(num):
    for num in list_of_numbers:
        if list_of_numbers[num] % 2 == 0:
            return list_even.append(num)
        else:
            return list_odd.append(num)
    return merge_two_list
       
print(list_even)
print(list_odd)
print(merge_two_list(list_of_numbers))