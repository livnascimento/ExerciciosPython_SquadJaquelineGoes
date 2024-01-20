contatos = {
  ("João da Silva", "(11) 9999-9999-1"),
  ("Maria Souza", "(11) 9999-9999-2"),
  ("José Santos", "(11) 9999-9999-3"),
  ("Ana Lima", "(11) 9999-9999-4"),
  ("Pedro Pereira", "(11) 9999-9999-5"),
  ("Clara Rodrigues", "(11) 9999-9999-6"),
  ("Carlos Lopes", "(11) 9999-9999-7"),
  ("Letícia Nunes", "(11) 9999-9999-8"),
  ("Rafaela Martins", "(11) 9999-9999-9"),
}

nome = input("Digite o nome.\n")

contatoEncontrado = False

for contato in contatos:
    if ( nome == contato[0]):
        contatoEncontrado = contato

if (contatoEncontrado):
    print(f"{contatoEncontrado[0]}: {contatoEncontrado[1]}")
else:
    print("Contato não encontrado.")