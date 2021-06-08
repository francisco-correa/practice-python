mix = [42, True, "towel", [2,1], 'hola', 34.4, {"name": "juan"}]

# for x in mix:
#     print(x)


# for value in mix:
#     print(type(value))

hello = []
for x in mix:
    if type(x) == dict:
        hello.append(x)
    if type(x) == list:
        hello.append(x)

print(hello)

