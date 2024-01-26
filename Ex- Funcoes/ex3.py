def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Bem-vindo ao Conversor de Temperatura!")
    
    while True:
        print("\nEscolha a opção de conversão:")
        print("1. Celsius para Fahrenheit")
        print("2. Fahrenheit para Celsius")
        

        escolha = input("Digite 1 ou 2: ")

        if escolha == '1':
            celsius = float(input("Digite a temperatura em Celsius: "))
            resultado = celsius_para_fahrenheit(celsius)
            print(f"{celsius} Celsius é igual a {resultado:.2f} Fahrenheit.")
    
        if escolha == '2':
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            resultado = fahrenheit_para_celsius(fahrenheit)
            print(f"{fahrenheit} Fahrenheit é igual a {resultado:.2f} Celsius.")
            break
        else:
            print("Escolha inválida. Por favor, digite 1 ou 2.")

if __name__ == "__main__":
    main()
