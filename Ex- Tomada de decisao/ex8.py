pares = 0
impares = 0

while True:
    numero = int(input("Digite um número.\n"))

    if (numero == 0):
        break

    if (numero % 2 == 0):
        pares += 1
    else:
        impares += 1

print(f"Você digitou {pares} números pares e {impares} números impares.")