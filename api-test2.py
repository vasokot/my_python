import requests
import sys
import json

url="https://api.artsy.net/api/artists/"


client_id='d76f609ba7211b800e4f'
client_secret='2f2a9fa607886365b3f59a53a13162af'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

d={}

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

with open("dataset.txt") as f:

    for line in f.readlines():

        req_url=url+line.strip()
        # инициируем запрос с заголовком
        r = requests.get(req_url, headers=headers)

        # разбираем ответ сервера
        j = json.loads(r.text)

        d[j['sortable_name']] = j['birthday']


d2= sorted(d.items(), key=lambda x: x[1])
print("===============")

print(d2)
#Выводим данные для проверки себя
for i in range(len(d2)):
    print(d2[i][0], d2[i][1])

#записываем данные, но передать их получилось только копи-пастом... хотя мб принял и файлом :)
with open("ans-api.txt",'w',encoding='utf-8',) as f:

    for i in range(len(d2)):
        s = d2[i][0]+'\n'
        f.write(s)

