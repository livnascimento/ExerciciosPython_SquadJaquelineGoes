horasExercicioPorSemana = int(input("Insira a quantidade de horas de exercício por semana.\n"))
horasExercicioPorMes = horasExercicioPorSemana * 4
minutosExercicioPorMes = horasExercicioPorSemana * 60

totalCaloriasMensal = minutosExercicioPorMes * 5

print(f"Você gasta, em média, {int(totalCaloriasMensal)} calorias por mês se exercitando.")
