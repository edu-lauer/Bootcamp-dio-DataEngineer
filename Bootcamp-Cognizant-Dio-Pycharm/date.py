from datetime import date, time, datetime

data_atual = date.today()
data_atual = data_atual.strftime('%d/%m/%y')

print(data_atual)

data_hora_atual = datetime.now()
data_hora_atual = data_hora_atual.strftime('%d/%m/%y %H:%M:%S')

print(data_hora_atual)

hora_atual = time(hour=19, minute=44, second=35)
print(hora_atual)
