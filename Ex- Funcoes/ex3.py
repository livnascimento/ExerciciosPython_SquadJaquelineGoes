def CelsiusParaFahrenheit(temperatura):
    print(f"{temperatura}°C equivale a {(temperatura * 9/5) + 32}°F")

def FahrenheitParaCelsius(temperatura):
    print(f"{temperatura}°F equivale a {temperatura - 32 * 5/9}°C")

def Menu():
    print("Escolha o tipo de conversão.")
    print("1- Celsius para Fahrenheit")
    print("2- Fahrenheit para celsius")

    opcao = input()

    temperatura = float(input("Digite a temperatura a converter.\n"))

    if (opcao == '1'):
        CelsiusParaFahrenheit(temperatura)
    elif (opcao == '2'):
        FahrenheitParaCelsius(temperatura)


Menu()