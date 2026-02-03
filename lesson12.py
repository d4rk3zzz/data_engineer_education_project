import requests
import pandas

YY = '2023'
MM = '11'
DD_int = 1
DD = f'{DD_int:02d}'
one_day = 1
list_for_csv = []
data = {}

if int(MM) == 12 or int(MM) == 5 or int(MM) == 1 or int(MM) == 3 or int(MM) == 7 or int(MM) == 8 or int(MM) == 10:
    mx_day = 31
elif int(MM) == 2 and (int(YY) % 4 == 0):
    mx_day = 29
elif int(MM) == 2 and (int(YY) % 4 != 0):
    mx_day = 28
else:
    mx_day = 30

while DD_int < mx_day + 1:
    try:
        print()
        print(f'{YY}/{MM}/{DD}')
        URL = f'https://www.cbr-xml-daily.ru/archive/{YY}/{MM}/{DD}/daily_json.js'
        r = requests.get(url=URL, timeout=10)
        r.raise_for_status()
        result = r.json()

        data['Дата'] = f'{YY}/{MM}/{DD}'
        data['Валюта'] = result.get('Valute').get('EUR').get('Name')
        data['Отношение к доллару'] = round((float(result.get('Valute').get('EUR').get('Value')) / float(result.get('Valute').get('USD').get('Value'))), 4)
        list_for_csv.append(data)
        data = {}

        data['Дата'] = f'{YY}/{MM}/{DD}'
        data['Валюта'] = 'Российский рубль'
        data['Отношение к доллару'] = round(float(result.get('Valute').get('USD').get('Value') ** - 1), 4)
        list_for_csv.append(data)
        data = {}

        print(result.get('Valute').get('USD').get('Name'), result.get('Valute').get('USD').get('Value'))
        print(result.get('Valute').get('EUR').get('Name'), result.get('Valute').get('EUR').get('Value'))
        print(result.get('Valute').get('CNY').get('Name'), result.get('Valute').get('CNY').get('Value'))
        DD_int += 1
        DD = f'{DD_int:02d}'
    except AttributeError:
        DD_int += 1
        DD = f'{DD_int:02d}'
        print('Был выходной, данных нет')
    except Exception as e:
        DD_int += 1
        DD = f'{DD_int:02d}'
        print(e)

df1 = pandas.DataFrame(list_for_csv)
df1.to_csv('valutes2023_11.csv', index=False)