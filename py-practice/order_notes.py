notes = [5.2, 5.9, 6.6, 6.6, 5.9, 5.9, 5.8]

notes.sort(reverse=True)
print(notes)

sort = sorted(notes)
print(sort)

def sum_all_values(sort):
    total= 0
    for x in sort:
        total += x
    return total
print(sum_all_values(sort))


def average(notes):
    sum = 0
    for x in notes:
        sum += x
    avg = sum/len(notes)
    return avg
print("El promedio es:", average(notes))