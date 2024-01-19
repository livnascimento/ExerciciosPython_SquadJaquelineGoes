salario = float(input("Por favor, digite o salário bruto.\n"))

if(salario < 1903.98):
    print("Isento de imposto de renda.")
elif (salario < 2826.65 ):
    aliquota = salario * (0.075)
    print(f"Alíquota de 7,5% equivalente a {aliquota}. Salário líquido: {salario - aliquota}")
elif (salario < 3751.05 ):
    aliquota = salario * (0.15)
    print(f"Alíquota de 15% equivalente a {aliquota}. Salário líquido: {salario - aliquota}")
elif (salario < 4664.68 ):
    aliquota = salario * (0.225)
    print(f"Alíquota de 22,5% equivalente a {aliquota}. Salário líquido: {salario - aliquota}")
else:
    aliquota = salario * (0.27)
    print(f"Alíquota de máxima de 27% equivalente a {aliquota}. Salário líquido: {salario - aliquota}")