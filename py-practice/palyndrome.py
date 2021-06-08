string = "ojos"

if str(string) == str(string)[::-1]:
    print("palindromo")
else:
    print("no es palindromo")

print("****************************************")
new_string = "Anita lava la tinA"
cadena = (new_string.replace(" ","")).lower()

if str(cadena) == str(cadena)[::-1]:
    print("palindromo")
else:
    print("no es palindromo")

print("****************************************")
def palindrome(word):
    new_word = word.replace(" ","").lower() 
    if new_word == new_word[::-1]:
        return "es palindromo"
    else:
        return "no es palindromo"

print(palindrome("Anita lAva lA tina"))