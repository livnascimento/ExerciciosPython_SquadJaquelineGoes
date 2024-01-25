print('Olá! Vamos calcular quantas calorias você queima em 1 mês.')

nome = input('Digite seu nome: ')
print(nome)

hora = int(input('Digite quantas horas de exercício físico você faz por semana: '))
semanas = int(4)
calorias = int(5)
calculo = (hora*60*5)*semanas

print (f'{nome}, você queima {calculo} calorias por mês.')