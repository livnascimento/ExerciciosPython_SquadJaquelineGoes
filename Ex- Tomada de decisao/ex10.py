print("Por favor, digite 3 números inteiros.")

numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

if (numero1 > numero2):
    aux = numero2
    numero2 = numero1
    numero1 = aux

if (numero2 > numero3):
    aux = numero3
    numero3 = numero2
    numero2 = aux

if (numero1 > numero2):
    aux = numero2
    numero2 = numero1
    numero1 = aux
    
print(numero1, numero2, numero3)