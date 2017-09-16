import csv
d = {}
with open("Crimes.csv") as cs_f:

    r =csv.reader(cs_f)

    for row in r:
        if row[5] not in d:
            d[row[5]]=0
        d[row[5]] +=1

print(d)

d2 = sorted(d.values())

print(d2)
print(max(d, key=lambda i: d[i]))