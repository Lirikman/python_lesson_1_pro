import requests

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
data = response.json()
print(data['Valute']['BYN']['Value'])

