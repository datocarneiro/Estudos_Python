
def comprimir_string(string):
    string_comprimida = ""
    quantidade = 1
    for i in range(1, len(string)):
        if string[i] ==  string[i-1]:
            quantidade += 1
        else:
            string_comprimida += str(quantidade) + string[i-1]
            quantidade = 1

    string_comprimida += str(quantidade) + string[i-1]
    return string_comprimida

string = "BBBBBBBBBAACCCDD"
print(comprimir_string(string))
    