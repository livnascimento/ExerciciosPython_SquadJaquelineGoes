print('Olá! Vamos calcular seu IMC.')

nome = input('Digite seu nome: ')
print(nome)

peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura em metros: '))
calculo = peso/(altura*altura)

print (f'{nome}, seu IMC é {calculo}.') 
      

