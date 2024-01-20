vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def contar_vogais (string):
    quantidadeVogais = 0
    for letra in string:
        if letra in vogais:
            quantidadeVogais += 1
    return quantidadeVogais

quantidadeVogais = contar_vogais("Eu me chamo Livia.")

print(f"Esta frase contém {quantidadeVogais} vogais")