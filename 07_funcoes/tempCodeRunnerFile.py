import datetime
from babel.dates import format_date
 
hoje=datetime.date.today()
data_extenso = format_date(hoje, format='long', locale='pt_br')
print(data_extenso)