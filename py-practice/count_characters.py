par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

my_clean = par.replace(" ", "")
counts = {}
for x in my_clean.lower():
    counts[x] = counts.get(x, 0) + 1

print(counts)

string = "holaaa"
contar = {}
for x in string:
    contar[x] = contar.get(x, 0) + 1
print(contar)

cadena = "fidsnjfnsdjkfnsdjfnsdjf"
print(len(cadena))


# definir una variable que borre los espacios
# definir diccionario vacio
# loop con metodo lowerCase
# definir el counts con metodo get y sumar uno total += total + 1
# imprimir el nuevo diccionario