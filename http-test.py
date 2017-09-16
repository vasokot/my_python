import requests
import re

cango = False

url1 = input()

req1 = requests.get(url1)

lst0=[]

pattern=r"""(<a\s[^>]*?href\s*=\s*['"])(\w+[:/]+)*([\w_\-.]+\.\w+)"""

for line0 in req1.text.splitlines():

    if re.findall(pattern,line0):
        ma= re.findall(pattern,line0,re.IGNORECASE)
        site0 = ma[0][2]
        if site0 not in lst0 and site0 !='..':
            lst0.append(site0.strip())

lst=sorted(lst0)

for site in lst:
    print(site)

