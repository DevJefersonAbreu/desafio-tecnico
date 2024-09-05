# 5. Programa que inverte os caracteres de uma string

def inverte_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

string = input("Digite uma string para inverter: ")
print("String invertida:", inverte_string(string))
