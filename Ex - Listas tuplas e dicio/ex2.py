medias = [0] * 5
alunosAprovados = 0

for i in range(5):
    media = 0
    print(f"Notas do aluno {i + 1}\n")
    for j in range(4):
        print(f"Nota {j + 1}:")
        nota = float(input())
        media += nota
    media /= 4
    medias[i] = media
    print(media)
    if (media >= 7):
        alunosAprovados += 1

print(f"O número de alunos aprovados é {alunosAprovados}")