idade = int(input("Por favor, digite sua idade.\n"))

if (idade <= 12):
    print("Criança.")
elif (idade < 18):
    print("Adolescente.")
elif (idade < 60):
    print("Adulto.")
else:
    print("Idoso.")