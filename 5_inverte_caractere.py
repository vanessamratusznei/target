'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de
sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

def inverter_string(string):
    l = len(string)
    string_invertida = ''
    i = l - 1
    while i >= 0:
        string_invertida += string[i]
        i -= 1
    return string_invertida

string_original = input("Digite uma string: ")
string_invertida = inverter_string(string_original)
print("String invertida:", string_invertida)
