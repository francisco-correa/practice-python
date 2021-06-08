names = ['Alice','Bob','Marry','Joe','Hilary','Stevia','Dylan']

def prepender(name):
    return "My name is: " + name
#Your code go here:
new_list = list(map(prepender, names))
print(new_list)


# var = list(map(function, list-var))
# print(var)