my_sample_list = [3423,5,4,47889,654,8,867543,23,48,5345,234,6,78,54,23,67,3,6,432,55,23,25,12]


def sum_all_values(items):
    total= 0
    for x in my_sample_list:
        total += x
    return total
print(sum_all_values(my_sample_list))


arr = [2, 4, 3]
sum(arr)
print(len(arr))
print(sum(arr))


def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma += i
    return laSuma

print(sumalista([1,3,5,7,9]))