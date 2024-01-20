perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

afirmativo = 0

for pergunta in perguntas:
    print(pergunta)
    resposta = input()
    if (resposta == 's'):
        afirmativo += 1

if (afirmativo < 2):
    print("Inocente.")
elif (afirmativo == 2):
    print("Suspeito.")
elif (afirmativo <= 4):
    print("Cúmplice.")
else:
    print("Assassino.")
