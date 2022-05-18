import csv

with open('./teste.csv', 'r', encoding='utf-8', newline='') as f:
    arq = csv.DictReader(f)
    data = {fieldname: [] for fieldname in arq.fieldnames}
    for row in arq:
        for fieldname, item in row.items():
            data[fieldname].append(item)
