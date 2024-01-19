notaInvalida = True

while (notaInvalida):
    nota = float(input("Digite a nota.\n"))
    if (nota > 0 and nota < 10):
        notaInvalida = False
    else:
        print("Nota inválida.")

print("Aprovado" if nota >= 7 else "Reprovado")