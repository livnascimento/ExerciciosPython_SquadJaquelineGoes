print("Digite 3 números diferentes")

numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

if (numero1 > numero2):
    maior = numero1
else:
    maior = numero2

if (numero3 > maior):
    maior = numero3

print(f"O maior número é {maior}")