import datetime
import calendar

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

dias_semana = [
    "segunda-feira", "terça-feira", "quarta-feira",
    "quinta-feira", "sexta-feira", "sábado", "domingo"
]

#21/12/2024
data = datetime.date(2024, 12, 21)

print(data)

hoje = datetime.date.today()

print(hoje)
print(hoje.strftime("%d/%m/%Y"))
print(f"{hoje.day} de {meses[hoje.month - 1]}  de {hoje.year}")
print(f"São Paulo, {dias_semana[hoje.weekday()]} {hoje.day} de {meses[hoje.month - 1]} de {hoje.year}")

#Ano é bissexto
print(f"2027 é Bissexto:{calendar.isleap(2027)}")

#Pega o ultimo dia do mês - pega a quantidade dia do mes com o parametro  ele me da o dia
print(f"É o ultimo dia do mês?  {calendar.monthrange(2026, 10)[1]}")

