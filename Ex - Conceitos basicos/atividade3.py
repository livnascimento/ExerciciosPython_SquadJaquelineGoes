
"""
Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.

"""


km = float(input("Digite a distância em quilômetros: "))


metros = km * 1000
centimetros = metros * 100
milimetros = metros * 1000


print(f"{km} quilômetros são equivalentes a:  {metros} metros, {centimetros} centímetros, {milimetros} milímetros  ")
