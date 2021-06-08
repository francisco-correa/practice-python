data = lambda x : x * 2
print(data(4))

def multiply(num):
    return lambda x : x * num
multiply_2 = multiply(2)
print(multiply_2(10))

suma = lambda x, y : x + y
print(suma(2,8))


#Creo un DataFrame con dos columnas, Celsius y Kelvin, ambas con datos iguales
data = {'Celsius':[22, 36, 20, 26, 30, 38],
        'Kelvin':[22, 36, 20, 26, 30, 38]}

#Creo una función Lambda para pasar los grados Celsius a Kelvin.
to_kelvin = lambda x: (x + 273,15)

print(to_kelvin(36))