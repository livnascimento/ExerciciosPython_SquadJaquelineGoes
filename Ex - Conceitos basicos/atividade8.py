print('Olá! Vamos calcular seu salário.')

nome = input('Digite seu nome: ')
print(nome)

hora = int(input('Digite quantas horas trabalha por dia: '))
dia = int(input('Digite quantos dias trabalha no mês: '))
valor = float(input('Digite quanto ganha por hora: '))
calculo = valor*(hora*dia)

print (f'{nome}, seu salário é de R${calculo}.')