import datetime

print("Digite seu ano de nascimento.")

anoDeNascimento = int(input())
anoAtual = datetime.date.today().year
mesAtual = datetime.date.today().month

idadeAtual = anoAtual - anoDeNascimento

print(f"Sua idade atual é {idadeAtual} (ou {idadeAtual - 1} se você nasceu depois do mês {mesAtual:02})")