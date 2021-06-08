num = int(input("enter a number: "))

if num % 2 == 0:
    print("es par")
else:
    print("impar")


def even_odd(number):
    for x in range(0, 51):
        if x % 2 == 0:
            print("es par")
        else:
            print("impar")

print(even_odd())
