import requests
import sys

url="http://numbersapi.com/"

params= {
    'json' : 'true'
}

with open("dataset.txt") as f:

    for line in f.readlines():
        req_url=url+line.strip()+'/math'
        req = requests.get(req_url,params=params)
        if req.status_code == 200:
            data = req.json()
            if data['found'] == True:
                print('Interesting')
            else:
                print('Boring')

