
'''"Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. 
Calcule e imprima o consumo médio em km/l."'''

# Recebe a quantidade de litros
litros_consumidos = float(input("Digite a quantidade de litros de combustível consumidos: "))

# recebe a distancia percorrida
distancia_percorrida = float(input("Digite a distância percorrida em quilômetros: "))

# valor final
consumo_medio = distancia_percorrida / litros_consumidos

print(f"O consumo médio é de {consumo_medio:.2f} km/l")