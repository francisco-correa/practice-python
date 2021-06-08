arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# def sum_odd_numbers(x):
total = 0
for x in range(len(arr)):
    if arr[x] % 2 != 0:
        total += arr[x]
print(total)

total_2 = 0
for x in range(len(arr)):
    if arr[x] % 2 == 0:
        total_2 += arr[x]
print(total_2)


print(total + total_2)